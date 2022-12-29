SHELL = bash
.PHONY := pack clean-packs mods clean-mod-jars clean-mod-zips clean-mods clean-all listmods genhelp genall clean clean-server server help

PY = $(shell which python3)
SCRIPT_SHOW_VERSION = $(PY) scripts/show_version.py
SCRIPT_DOWNLOAD_MODS = $(PY) scripts/download_mods.py
SCRIPT_GENERATE_MODS_LIST = $(PY) scripts/generate_mods_list.py
SCRIPT_SHOW_BUILD_DIR = $(PY) scripts/show_build_dir.py
SCRIPT_SHOW_GAME_VERSION = $(PY) scripts/show_game_version.py
SCRIPT_SHOW_FABRIC_VERSION = $(PY) scripts/show_fabric_version.py

VERSION = $(shell $(SCRIPT_SHOW_VERSION))
BUILD_DIR = $(shell $(SCRIPT_SHOW_BUILD_DIR))
GAME_VERSION = $(shell $(SCRIPT_SHOW_GAME_VERSION))
FABRIC_VERSION = $(shell $(SCRIPT_SHOW_FABRIC_VERSION))
HOW_TO_USE_MAKEFILE_MD = HOW-TO-USE-MAKEFILE.md

### pack:                Generates the modpack zip for client which includes "overrides" and manifest.json
pack:
	@zip $(BUILD_DIR)/modpack/Dirty-Craft-$(VERSION).zip -r overrides pack.png manifest.json
	@echo Modpack file $(BUILD_DIR)/modpack/Dirty-Craft-$(VERSION).zip generated successfully

### mods:                Downloads all of the mods defined in manifest.json from the curseforge and compresses them into a zip file
mods:
	@$(SCRIPT_DOWNLOAD_MODS) $(VERSION)

### server:              Generates the modpack for server
server: mods
	@echo "Preparing..."
	-@rm -rf $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server
	-@rm -rf $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server.zip
	@mkdir $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server
	@echo "Copying overrides files..."
	-@cp overrides/* $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server -ar
	@echo "Done"
	@echo "Copying mods..."
	@mkdir $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server/mods
	@unzip $(BUILD_DIR)/mods/zip/Dirty-Craft-$(VERSION)-mods.zip -d $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server/mods
	@echo "Done"
	@echo "Downloading fabric..."
	@wget -c https://meta.fabricmc.net/v2/versions/loader/$(GAME_VERSION)/$(FABRIC_VERSION)/0.11.1/server/jar -O $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server/fabric.jar
	@echo "Done"
	@echo "Making the zip file..."
	@mv $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server .
	@zip $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server.zip -r Dirty-Craft-$(VERSION)-server
	@echo "Done"
	@echo "Cleaning up..."
	-@rm -rf Dirty-Craft-$(VERSION)-server
	@echo "The server pack generated successfully in $(BUILD_DIR)/server/Dirty-Craft-$(VERSION)-server.zip"

### listmods:            Generates list of the installed mods in the modpack in MODS.md file
listmods:
	@$(SCRIPT_GENERATE_MODS_LIST)

### genhelp:             Generates this makefile help in HOW_TO_USE_MAKEFILE_MD
genhelp:
	@echo "# This is a guide for the Makefile in this project" > $(HOW_TO_USE_MAKEFILE_MD)
	@echo >> $(HOW_TO_USE_MAKEFILE_MD)
	@cat Makefile | grep "###" | grep -v "cat Makefile | grep " >> $(HOW_TO_USE_MAKEFILE_MD)
	@echo "Makefile guide generated successfully"

### help:                Shows this help
help:
	@cat Makefile | grep "###" | grep -v "cat Makefile | grep "

### genall:              Generates all of the generatable source code files (like mods list, helps, etc.)
genall: listmods genhelp

### clean-packs:         Removes the generated modpack zip files
clean-packs:
	-rm $(BUILD_DIR)/modpack/*.zip

### clean-mod-jars:      Deletes the downloaded mod jar files
clean-mod-jars:
	-rm $(BUILD_DIR)/mods/jar/*.jar

### clean-mod-zips:      Deletes the compressed mods zip files
clean-mod-zips:
	-rm $(BUILD_DIR)/mods/zip/*.zip

### clean-mods:          Deletes both downloaded jars and created mods zip files
clean-mods: clean-mod-jars clean-mod-zips

### clean-server:        Cleans server pack generated zip files
clean-server:
	-rm $(BUILD_DIR)/server/*.zip

### clean:               Cleans all of the generated files but not downloaded mod files
clean: clean-packs clean-mod-zips clean-server

### clean-all:           Cleans everything and deletes all of the downloaded and generated files
clean-all: clean-packs clean-mods clean-server
