# This is a guide for the Makefile in this project

### pack                Generates the modpack zip for client which includes "overrides" and manifest.json
### mods                Downloads all of the mods defined in manifest.json from the curseforge and compresses them into a zip file
### listmods            Generates list of the installed mods in the modpack in MODS.md file
### genhelp             Generates this makefile help in HOW_TO_USE_MAKEFILE_MD
### genall              Generates all of the generatable source code files (like mods list, helps, etc.)
### clean-packs         Removes the generated modpack zip files
### clean-mod-jars      Deletes the downloaded mod jar files
### clean-mod-zips      Deletes the compressed mods zip files
### clean-mods          Deletes both downloaded jars and created mods zip files
### clean-all           Cleans everything and deletes all of the downloaded and generated files