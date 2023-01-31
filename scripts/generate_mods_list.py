import tools

content = '# Mods list\n\n'
content += 'There are ' + str(len(tools.load_manifest()['files'])) + ' mods installed in Dirty Craft (' + tools.get_version() + ') modpack:\n\n'

for mod in tools.load_manifest()['files']:
    link = 'https://www.curseforge.com/minecraft/mc-mods/' + str(mod['link_slug'])
    content += '- [' + mod['filename'] + '](' + link + ')\n'

mods_list_file = open('MODS.md', 'w')
mods_list_file.write(content)
mods_list_file.close()

print('Mods list has been generated in MODS.md')
