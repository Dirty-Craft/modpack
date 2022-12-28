import os
import sys
import json


VERSION = 'dev'
if len(sys.argv) > 1:
    VERSION = sys.argv[1]


def download_once(mod):
    file_id = str(mod['fileID'])
    id_1 = str(int(file_id[:4]))
    id_2 = str(int(file_id[4:]))

    url = 'https://mediafilez.forgecdn.net/files/' + id_1 + '/' + id_2 + '/' + mod['filename'].replace('+', '%2B')

    command = 'wget -c --header "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0" "' + url + '"'

    os.system(command)

if not os.path.isfile('manifest.json'):
    print('Couldn\'t find file "manifest.json"')
    sys.exit(1)


manifest_file = open('manifest.json', 'r')
content = json.load(manifest_file)
manifest_file.close()


downloaded_jars = []
real_cwd = os.getcwd()
os.chdir('output/mods/jar')
for f in content['files'][::-1]:
    download_once(f)
    downloaded_jars.append('"' + f['filename'] + '"')

os.system('zip ../zip/Dirty-Craft-' + VERSION + '-mods.zip -r ' + ' '.join(downloaded_jars))

os.chdir(real_cwd)
