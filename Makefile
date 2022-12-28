SHELL = bash
.PHONY := pack clean-packs mods clean-mod-jars clean-mod-zips clean-mods clean-all listmods genhelp genall

PY = $(shell which python3)
SCRIPT_SHOW_VERSION = $(PY) scripts/show_version.py
SCRIPT_DOWNLOAD_MODS = $(PY) scripts/download_mods.py
SCRIPT_GENERATE_MODS_LIST = $(PY) scripts/generate_mods_list.py

VERSION = $(shell $(SCRIPT_SHOW_VERSION))
HOW_TO_USE_MAKEFILE_MD = HOW-TO-USE-MAKEFILE.md

### pack                Generates the modpack zip for client which includes "overrides" and manifest.json
pack:
	@zip output/modpack/Dirty-Craft-$(VERSION).zip -r overrides pack.png manifest.json
	@echo Modpack file output/modpack/Dirty-Craft-$(VERSION).zip generated successfully

### mods                Downloads all of the mods defined in manifest.json from the curseforge and compresses them into a zip file
mods:
	@$(SCRIPT_DOWNLOAD_MODS) $(VERSION)

### listmods            Generates list of the installed mods in the modpack in MODS.md file
listmods:
	@$(SCRIPT_GENERATE_MODS_LIST)

### genhelp             Generates this makefile help in HOW_TO_USE_MAKEFILE_MD
genhelp:
	@echo "# This is a guide for the Makefile in this project" > $(HOW_TO_USE_MAKEFILE_MD)
	@echo >> $(HOW_TO_USE_MAKEFILE_MD)
	@cat Makefile | grep "###" | grep -v "cat Makefile | grep " >> $(HOW_TO_USE_MAKEFILE_MD)
	@echo "Makefile guide generated successfully"

### genall              Generates all of the generatable source code files (like mods list, helps, etc.)
genall: listmods genhelp

### clean-packs         Removes the generated modpack zip files
clean-packs:
	-rm output/modpack/*.zip

### clean-mod-jars      Deletes the downloaded mod jar files
clean-mod-jars:
	-rm output/mods/jar/*.jar

### clean-mod-zips      Deletes the compressed mods zip files
clean-mod-zips:
	-rm output/mods/zip/*.zip

### clean-mods          Deletes both downloaded jars and created mods zip files
clean-mods: clean-mod-jars clean-mod-zips

### clean-all           Cleans everything and deletes all of the downloaded and generated files
clean-all: clean-packs clean-mods
