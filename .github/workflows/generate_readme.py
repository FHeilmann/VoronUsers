#!python3
from pathlib import Path
import yaml
import textwrap

preamble = """
# Mods

Printer mods for Voron 3D printers

## Legacy printers

Mods for legacy printers can be found [here](../legacy_printers/printer_mods).
If one of your legacy mods applies to a current Voron 3D printer and therefore should be included in this list, 
contact the admins on Discord to have your mod moved to this folder.

---

| Creator | Mod title | Description | Printer compatibility |
"""
yaml_list = Path("printer_mods").glob("**/.metadata.yml")
print(preamble)
prev_username = ""
for yml in yaml_list:
    with open(yml, 'r') as f:
        content = yaml.safe_load(f)
        title = textwrap.shorten(content["title"], width=35, placeholder="...")
        creator = yml.parts[1] if {yml.parts[1]} != prev_username else ""
        description = textwrap.shorten(content["description"], width=70, placeholder="...")
        print(f'| {creator} | [{title}]({yml.relative_to("printer_mods").parent}) | {description} | {", ".join(sorted(content["printer_compatibility"]))} |')
        prev_username = yml.parts[1]
print("\n")