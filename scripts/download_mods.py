import tools


def download_once(mod):
    file_id = str(mod['fileID'])
    id_1 = str(int(file_id[:4]))
    id_2 = str(int(file_id[4:]))
    url = 'https://mediafilez.forgecdn.net/files/' + id_1 + '/' + id_2 + '/' + mod['filename'].replace('+', '%2B')
    command = 'wget -c --header "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0" "' + url + '"'
    tools.os.system(command)


content = tools.load_manifest()
downloaded_jars = []
real_cwd = tools.os.getcwd()
version = tools.get_version()
tools.os.chdir(tools.BUILD_DIR + '/mods/jar')

for f in content['files'][::-1]:
    download_once(f)
    downloaded_jars.append('"' + f['filename'] + '"')

tools.os.system('zip ../zip/Dirty-Craft-' + version + '-mods.zip -r ' + ' '.join(downloaded_jars))
tools.os.chdir(real_cwd)

print('All of the mods downloaded successfully and compressed in ' + tools.BUILD_DIR + '/mods/zip/Dirty-Craft-' + version + '-mods.zip')
