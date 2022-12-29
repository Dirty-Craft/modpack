# This is a guide for the Makefile in this project

### pack:                Generates the modpack zip for client which includes "overrides" and manifest.json
### mods:                Downloads all of the mods defined in manifest.json from the curseforge and compresses them into a zip file
### server:              Generates the modpack for server
### listmods:            Generates list of the installed mods in the modpack in MODS.md file
### genhelp:             Generates this makefile help in HOW_TO_USE_MAKEFILE_MD
### help:                Shows this help
### genall:              Generates all of the generatable source code files (like mods list, helps, etc.)
### clean-packs:         Removes the generated modpack zip files
### clean-mod-jars:      Deletes the downloaded mod jar files
### clean-mod-zips:      Deletes the compressed mods zip files
### clean-mods:          Deletes both downloaded jars and created mods zip files
### clean-server:        Cleans server pack generated zip files
### clean:               Cleans all of the generated files but not downloaded mod files
### clean-all:           Cleans everything and deletes all of the downloaded and generated files
