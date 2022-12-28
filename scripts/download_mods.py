import os
import sys
import json


def download_once(mod):
    file_id = str(mod['fileID'])
    id_1 = str(int(file_id[:4]))
    id_2 = str(int(file_id[4:]))

    url = 'https://mediafilez.forgecdn.net/files/'+id_1+'/'+id_2+'/' + mod['filename']

    command = 'wget --header "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0" "'+url+'"'

    os.system(command)

if not os.path.isfile('manifest.json'):
    print('Couldn\'t find file "manifest.json"')
    sys.exit(1)


manifest_file = open('manifest.json', 'r')
content = json.load(manifest_file)
manifest_file.close()


real_cwd = os.getcwd()
os.chdir('output/downloads')
for f in content['files']:
    download_once(f)

os.system('zip Dirty-Craft-1.19.2_0.0.1-mods.zip -r *.jar')
os.system('rm *.jar')

os.chdir(real_cwd)
