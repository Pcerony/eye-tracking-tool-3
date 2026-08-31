import json

manifest = json.load(open('deck-manifest.json', 'r', encoding='utf-8'))
for slide in manifest['slides']:
    if slide['id'] in [
        's18a-entropy-intro',
        's18b-conventional-metrics',
        's18c-cognitive-friction',
        's18d-surprisal-theory',
        's18e-case-information-weight',
        's18f-cognitive-gain-formula',
        's18g-markov-stagnation',
        's18h-efficiency-ratio'
    ]:
        slide['assets'] = []

json.dump(manifest, open('deck-manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("Updated deck-manifest.json assets list.")
