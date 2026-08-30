# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
import json
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONSOLIDATED_JSON = os.path.join(BASE_DIR, 'data', 'consolidated', 'all_13_participants_archive.json')
ASSETS_DIR = os.path.join(BASE_DIR, 'src', 'assets', 'images')
OUTPUTS_DIR = os.path.join(BASE_DIR, 'outputs', 'entropy_analysis')

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# 1. Load data
with open(CONSOLIDATED_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Compute metrics
AOI_DEFS = {
    'a1': {'aois': [{'id': 'text', 'box': [0.48, 0.28, 0.44, 0.64]}, {'id': 'photo', 'box': [0.08, 0.28, 0.36, 0.64]}]},
    'a2': {'aois': [{'id': 'tactile_bubble', 'box': [0.08, 0.58, 0.84, 0.38]}, {'id': 'text_module', 'box': [0.48, 0.26, 0.44, 0.30]}, {'id': 'photo', 'box': [0.08, 0.26, 0.36, 0.30]}]},
    'b1': {'aois': [{'id': 'text', 'box': [0.48, 0.28, 0.44, 0.64]}, {'id': 'photo', 'box': [0.08, 0.28, 0.36, 0.64]}]},
    'b2': {'aois': [{'id': 'sensory_bubble', 'box': [0.08, 0.58, 0.84, 0.38]}, {'id': 'dialogue', 'box': [0.48, 0.26, 0.44, 0.30]}, {'id': 'photo', 'box': [0.08, 0.26, 0.36, 0.30]}]}
}

SURPRISAL_WEIGHTS = {
    'a1': {'text': 0.415, 'photo': 1.000, 'background': 0.500},
    'a2': {'tactile_bubble': 3.059, 'text_module': 0.415, 'photo': 1.000, 'background': 0.500},
    'b1': {'text': 0.415, 'photo': 1.000, 'background': 0.500},
    'b2': {'sensory_bubble': 3.059, 'dialogue': 2.737, 'photo': 1.000, 'background': 0.500}
}

DESIGN_INTENTS = {
    'a1': {'text': 0.45, 'photo': 0.45, 'background': 0.10},
    'a2': {'tactile_bubble': 0.40, 'text_module': 0.20, 'photo': 0.30, 'background': 0.10},
    'b1': {'text': 0.45, 'photo': 0.45, 'background': 0.10},
    'b2': {'sensory_bubble': 0.40, 'dialogue': 0.25, 'photo': 0.25, 'background': 0.10}
}

def get_point_aoi(x, y, image_id):
    aois = AOI_DEFS.get(image_id, {}).get('aois', [])
    for aoi in aois:
        bx, by, bw, bh = aoi['box']
        if bx <= x <= bx + bw and by <= y <= by + bh:
            return aoi['id']
    return 'background'

def calculate_shannon_entropy(prob_dist):
    h = 0.0
    for p in prob_dist.values():
        if p > 1e-12:
            h -= p * math.log2(p)
    return h

def calculate_transition_entropy(aoi_seq, all_aois):
    if len(aoi_seq) < 2:
        return 0.0, np.zeros((len(all_aois), len(all_aois)))
    aoi_idx = {aoi: i for i, aoi in enumerate(all_aois)}
    K = len(all_aois)
    trans_counts = np.zeros((K, K))
    for i in range(len(aoi_seq) - 1):
        src = aoi_seq[i]
        dst = aoi_seq[i+1]
        trans_counts[aoi_idx[src], aoi_idx[dst]] += 1
    row_sums = trans_counts.sum(axis=1, keepdims=True)
    with np.errstate(divide='ignore', invalid='ignore'):
        trans_matrix = np.where(row_sums > 0, trans_counts / row_sums, 0.0)
    
    total_transitions = len(aoi_seq) - 1
    src_counts = {aoi: 0 for aoi in all_aois}
    for i in range(len(aoi_seq) - 1):
        src_counts[aoi_seq[i]] += 1
    pi = np.array([src_counts[aoi] / total_transitions for aoi in all_aois])
    
    gte = 0.0
    for i in range(K):
        if pi[i] > 1e-12:
            for j in range(K):
                p_ij = trans_matrix[i, j]
                if p_ij > 1e-12:
                    gte -= pi[i] * p_ij * math.log2(p_ij)
    return gte, trans_matrix

def calculate_kl_divergence(p_dist, q_dist, all_aois, eps=1e-6):
    kl = 0.0
    for aoi in all_aois:
        p = p_dist.get(aoi, 0.0)
        q = q_dist.get(aoi, eps)
        if p > 1e-12:
            kl += p * math.log2(p / q)
    return max(0.0, kl)

participant_pairs = {}
sessions = data.get('sessions', [])
for session in sessions:
    p_id = session.get('id') or session.get('label')
    runs = session.get('runs', [])
    for run in runs:
        img_id = (run.get('imageName') or run.get('image', {}).get('id') or run.get('image', {}).get('name') or '').lower()
        cond_raw = (run.get('condition') or '').lower()
        if img_id in ['a1', 'b1'] or 'control' in cond_raw or '对照' in cond_raw:
            condition = 'control'
            if not img_id: img_id = 'a1' if session.get('group') == 'A' else 'b1'
        elif img_id in ['a2', 'b2'] or 'experiment' in cond_raw or 'intervention' in cond_raw or '实验' in cond_raw:
            condition = 'intervention'
            if not img_id: img_id = 'a2' if session.get('group') == 'A' else 'b2'
        else:
            continue
        points = run.get('points', [])
        valid_points = [p for p in points if p.get('onPaper') and 0.0 <= p.get('a4X', -1) <= 1.0 and 0.0 <= p.get('a4Y', -1) <= 1.0]
        if len(valid_points) < 10: continue
        aoi_seq = [get_point_aoi(p['a4X'], p['a4Y'], img_id) for p in valid_points]
        img_aoi_defs = AOI_DEFS.get(img_id, {}).get('aois', [])
        all_aoi_keys = [a['id'] for a in img_aoi_defs] + ['background']
        K = len(all_aoi_keys)
        aoi_counts = {aoi: aoi_seq.count(aoi) for aoi in all_aoi_keys}
        total_pts = len(aoi_seq)
        p_gaze = {aoi: aoi_counts[aoi] / total_pts for aoi in all_aoi_keys}
        sge = calculate_shannon_entropy(p_gaze)
        norm_sge = sge / math.log2(K) if K > 1 else 0.0
        gte, trans_mat = calculate_transition_entropy(aoi_seq, all_aoi_keys)
        norm_gte = gte / math.log2(K) if K > 1 else 0.0
        surprisal_dict = SURPRISAL_WEIGHTS.get(img_id, {})
        e_gain = sum(p_gaze[aoi] * surprisal_dict.get(aoi, 0.5) for aoi in all_aoi_keys)
        eta = e_gain / (gte + 0.1)
        q_intent = DESIGN_INTENTS.get(img_id, {})
        d_kl = calculate_kl_divergence(p_gaze, q_intent, all_aoi_keys)
        record = {
            'participant': p_id,
            'sge': sge,
            'normSge': norm_sge,
            'gte': gte,
            'normGte': norm_gte,
            'eGain': e_gain,
            'eta': eta,
            'dKl': d_kl
        }
        if p_id not in participant_pairs: participant_pairs[p_id] = {}
        participant_pairs[p_id][condition] = record

# Extract pairs
paired = {'gte': [], 'eGain': [], 'eta': [], 'sge': [], 'normSge': [], 'dKl': []}
for p_id, d in participant_pairs.items():
    if 'control' in d and 'intervention' in d:
        c, i = d['control'], d['intervention']
        for k in paired.keys():
            paired[k].append((c[k], i[k]))

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Helvetica', 'Arial']
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 1.2

c_ctrl = '#64748b'
c_intv = '#059669'

# 1. Chart A: GTE
fig, ax = plt.subplots(figsize=(7.5, 5.2), dpi=300)
for c_val, i_val in paired['gte']:
    ax.plot([1, 2], [c_val, i_val], color='#94a3b8', alpha=0.65, linewidth=1.8, zorder=1)
    ax.scatter([1], [c_val], color=c_ctrl, s=80, alpha=0.9, zorder=2)
    ax.scatter([2], [i_val], color=c_intv, s=80, alpha=0.9, zorder=2)
m_c, m_i = np.mean([p[0] for p in paired['gte']]), np.mean([p[1] for p in paired['gte']])
s_c, s_i = np.std([p[0] for p in paired['gte']], ddof=1), np.std([p[1] for p in paired['gte']], ddof=1)
ax.errorbar([0.72, 2.28], [m_c, m_i], yerr=[s_c, s_i], fmt='o', color='#0f172a', elinewidth=2.8, capsize=8, markersize=10, zorder=3)
ax.set_xticks([1, 2])
ax.set_xticklabels(['Control (A1/B1)\nTraditional Signage', 'Intervention (A2/B2)\nCo-created Signage'], fontsize=12, fontweight='bold')
ax.set_title('Gaze Transition Entropy (GTE)\n[Path Randomness & Cross-AOI Exploration]', fontsize=14, fontweight='bold', pad=12)
ax.set_ylabel('Transition Entropy (bits)', fontsize=12, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
p_gte = os.path.join(ASSETS_DIR, 'entropy-chart-gte.png')
plt.savefig(p_gte)
plt.close()

# 2. Chart B: E_gain
fig, ax = plt.subplots(figsize=(7.5, 5.2), dpi=300)
for c_val, i_val in paired['eGain']:
    ax.plot([1, 2], [c_val, i_val], color='#10b981', alpha=0.75, linewidth=2.0, zorder=1)
    ax.scatter([1], [c_val], color=c_ctrl, s=80, alpha=0.9, zorder=2)
    ax.scatter([2], [i_val], color=c_intv, s=80, alpha=0.9, zorder=2)
m_c, m_i = np.mean([p[0] for p in paired['eGain']]), np.mean([p[1] for p in paired['eGain']])
s_c, s_i = np.std([p[0] for p in paired['eGain']], ddof=1), np.std([p[1] for p in paired['eGain']], ddof=1)
ax.errorbar([0.72, 2.28], [m_c, m_i], yerr=[s_c, s_i], fmt='o', color='#0f172a', elinewidth=2.8, capsize=8, markersize=10, zorder=3)
ax.set_xticks([1, 2])
ax.set_xticklabels(['Control (A1/B1)\nTraditional Signage', 'Intervention (A2/B2)\nCo-created Signage'], fontsize=12, fontweight='bold')
ax.set_title('Information-Weighted Cognitive Gain ($E_{gain}$)\n[Surprisal & Effective Knowledge Yield]', fontsize=14, fontweight='bold', pad=12)
ax.set_ylabel('Expected Surprisal Gain (bits)', fontsize=12, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
p_egain = os.path.join(ASSETS_DIR, 'entropy-chart-egain.png')
plt.savefig(p_egain)
plt.close()

# 3. Chart C: eta
fig, ax = plt.subplots(figsize=(7.5, 5.2), dpi=300)
for c_val, i_val in paired['eta']:
    ax.plot([1, 2], [c_val, i_val], color='#f97316', alpha=0.75, linewidth=1.8, zorder=1)
    ax.scatter([1], [c_val], color=c_ctrl, s=80, alpha=0.9, zorder=2)
    ax.scatter([2], [i_val], color='#ea580c', s=80, alpha=0.9, zorder=2)
m_c, m_i = np.mean([p[0] for p in paired['eta']]), np.mean([p[1] for p in paired['eta']])
s_c, s_i = np.std([p[0] for p in paired['eta']], ddof=1), np.std([p[1] for p in paired['eta']], ddof=1)
ax.errorbar([0.72, 2.28], [m_c, m_i], yerr=[s_c, s_i], fmt='o', color='#0f172a', elinewidth=2.8, capsize=8, markersize=10, zorder=3)
ax.set_xticks([1, 2])
ax.set_xticklabels(['Control (A1/B1)\nTraditional Signage', 'Intervention (A2/B2)\nCo-created Signage'], fontsize=12, fontweight='bold')
ax.set_title('Cognitive Information Efficiency ($\eta = E_{gain} / GTE$)\n[Knowledge Absorbed per Unit Visual Search Effort]', fontsize=14, fontweight='bold', pad=12)
ax.set_ylabel('Efficiency Ratio $\eta$ (bits/bit)', fontsize=12, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
p_eta = os.path.join(ASSETS_DIR, 'entropy-chart-eta.png')
plt.savefig(p_eta)
plt.close()

# 4. Chart D: SGE & KL
fig, ax = plt.subplots(figsize=(7.5, 5.2), dpi=300)
labels = ['SGE (Raw)', 'Norm SGE', '$D_{KL}$ (Intent)']
x = np.arange(len(labels))
width = 0.35
m_sge_c, m_sge_i = np.mean([p[0] for p in paired['sge']]), np.mean([p[1] for p in paired['sge']])
s_sge_c, s_sge_i = np.std([p[0] for p in paired['sge']], ddof=1), np.std([p[1] for p in paired['sge']], ddof=1)
m_nsge_c, m_nsge_i = np.mean([p[0] for p in paired['normSge']]), np.mean([p[1] for p in paired['normSge']])
s_nsge_c, s_nsge_i = np.std([p[0] for p in paired['normSge']], ddof=1), np.std([p[1] for p in paired['normSge']], ddof=1)
m_dkl_c, m_dkl_i = np.mean([p[0] for p in paired['dKl']]), np.mean([p[1] for p in paired['dKl']])
s_dkl_c, s_dkl_i = np.std([p[0] for p in paired['dKl']], ddof=1), np.std([p[1] for p in paired['dKl']], ddof=1)

rects1 = ax.bar(x - width/2, [m_sge_c, m_nsge_c, m_dkl_c], width, yerr=[s_sge_c, s_nsge_c, s_dkl_c], label='Control (A1/B1)', color='#64748b', capsize=6)
rects2 = ax.bar(x + width/2, [m_sge_i, m_nsge_i, m_dkl_i], width, yerr=[s_sge_i, s_nsge_i, s_dkl_i], label='Intervention (A2/B2)', color='#059669', capsize=6)

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12, fontweight='bold')
ax.set_title('Spatial Gaze Structure & Design Intent Alignment\n[Balanced Exploration and Intent Convergence]', fontsize=14, fontweight='bold', pad=12)
ax.set_ylabel('Entropy / Divergence (bits)', fontsize=12, fontweight='bold')
ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
p_sge = os.path.join(ASSETS_DIR, 'entropy-chart-sge.png')
plt.savefig(p_sge)
plt.close()

print(f"[*] 4 个高清独立图表已成功输出至: {ASSETS_DIR}")
