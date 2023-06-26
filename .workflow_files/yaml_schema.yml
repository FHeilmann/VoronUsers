---
name: VoronUsers metadata schema
desc: Schema used for validation of .metadata.yml files in the VoronUsers repository

type: map
mapping:
    title:
      type: str
      required: True
    description:
      type: str
      required: True
    printer_compatibility:
      type: seq
      required: True
      sequence:
        - type: str
          enum: ["V0", "V1", "V2", "VSW", "Trident"]
    images:
      type: seq
      required: False
      sequence:
        - type: str
    cad:
      type: seq
      required: True
      sequence:
        - type: str
    discord_username:
      required: False
      type: str