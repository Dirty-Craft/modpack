modpack:
	zip output/dirty-craft.zip -r overrides pack.png manifest.json

download:
	python3 scripts/download_mods.py
