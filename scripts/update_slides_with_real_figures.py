import json
import os

# 1. Update deck-manifest.json assets and slide assets
with open('deck-manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

new_assets = [
    {"id": "entropy-fig-01-paradigm", "path": "src/assets/images/entropy-fig-01-paradigm.jpg", "access": "public"},
    {"id": "entropy-fig-02-metrics-flaw", "path": "src/assets/images/entropy-fig-02-metrics-flaw.jpg", "access": "public"},
    {"id": "entropy-fig-03-friction", "path": "src/assets/images/entropy-fig-03-friction.jpg", "access": "public"},
    {"id": "entropy-fig-04-surprisal", "path": "src/assets/images/entropy-fig-04-surprisal.jpg", "access": "public"},
    {"id": "entropy-fig-05-aoi-weights", "path": "src/assets/images/entropy-fig-05-aoi-weights.jpg", "access": "public"},
    {"id": "entropy-fig-06-egain-walkthrough", "path": "src/assets/images/entropy-fig-06-egain-walkthrough.jpg", "access": "public"},
    {"id": "entropy-fig-07-markov-flow", "path": "src/assets/images/entropy-fig-07-markov-flow.jpg", "access": "public"},
    {"id": "entropy-fig-08-eta-efficiency", "path": "src/assets/images/entropy-fig-08-eta-efficiency.jpg", "access": "public"}
]

existing_asset_ids = {a['id'] for a in manifest['assets']}
for na in new_assets:
    if na['id'] not in existing_asset_ids:
        manifest['assets'].append(na)

# Update slide assets mapping in manifest
slide_asset_map = {
    "s18a-entropy-intro": ["entropy-fig-01-paradigm"],
    "s18b-conventional-metrics": ["entropy-fig-02-metrics-flaw"],
    "s18c-cognitive-friction": ["entropy-fig-03-friction"],
    "s18d-surprisal-theory": ["entropy-fig-04-surprisal"],
    "s18e-case-information-weight": ["entropy-fig-05-aoi-weights"],
    "s18f-cognitive-gain-formula": ["entropy-fig-06-egain-walkthrough"],
    "s18g-markov-stagnation": ["entropy-fig-07-markov-flow"],
    "s18h-efficiency-ratio": ["entropy-fig-08-eta-efficiency"]
}

for s in manifest['slides']:
    if s['id'] in slide_asset_map:
        s['assets'] = slide_asset_map[s['id']]

with open('deck-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print("Updated deck-manifest.json assets successfully!")
