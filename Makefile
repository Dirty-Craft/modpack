VERSION = $(shell cat version.txt)

pack:
	zip output/modpack/Dirty-Craft-$(VERSION).zip -r overrides pack.png manifest.json

mods:
	python3 scripts/download_mods.py $(VERSION)
