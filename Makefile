VERSION = $(shell cat version.txt)

pack:
	zip output/modpack/Dirty-Craft-$(VERSION).zip -r overrides pack.png manifest.json

clean-packs:
	-rm output/modpack/*.zip

mods:
	python3 scripts/download_mods.py $(VERSION)

clean-mod-jars:
	-rm output/mods/jar/*.jar

clean-mod-zips:
	-rm output/mods/zip/*.zip

clean-mods: clean-mod-jars clean-mod-zips

clean: clean-packs clean-mods
