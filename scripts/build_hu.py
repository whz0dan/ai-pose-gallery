"""Build the Hungarian catalog from the English metadata; never fetch images."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
translations = json.loads((ROOT / 'scripts/hu-translations.json').read_text())
source = json.loads((ROOT / 'data/pose-en.json').read_text())
result = []
for entry in source:
    item = dict(entry)
    item['name_en'] = entry['name']
    item['category_en'] = entry['category']
    item['system_en'] = entry['system']
    for field, section in [('name', 'names'), ('category', 'categories'),
                           ('system', 'systems'), ('angle', 'angles')]:
        item[field] = translations[section][entry[field]]
    result.append(item)
(ROOT / 'data/pose-hu.json').write_text(
    json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n')
print(f'{len(result)} nézet magyar fordítása elkészült.')
