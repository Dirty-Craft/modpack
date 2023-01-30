import tools
import sys
from pprint import pprint
import requests
import json


def is_already_added(mod_id):
    for item in tools.load_manifest()['files']:
        if str(item['projectID']) == str(mod_id):
            return True
    return False


def add_once(slug):
    try:
        result = tools.call_curseforge_api('mods/search?gameId=' + tools.CURSEFORGE_MINECRAFT_GAME_ID + '&classId=' + tools.CURSEFORGE_MINECRAFT_MODS_CLASS_ID + '&slug=' + slug)
        result = result['data'][0]
    except Exception as ex:
        print('error: failed to load slug "' + slug + '": ' + str(ex))
        return

    msg = ('Loading project ID ' + str(result['id']) + ' (' + result['slug'] + ')')
    print('=' * len(msg))
    print(msg)

    if is_already_added(result['id']):
        print('This mod is already installed. Skipping...')
        return

    item_to_add_to_manifest = {
        "filename": "",
        "link_slug": result['slug'],
        "projectID": result['id'],
        "fileID": 0,
        "required": True,
    }

    files_list = tools.call_curseforge_api('mods/' + str(result['id']) + '/files')['data']
    files_list.reverse()

    print('Select the file you want to add to the modpack:')
    i = 0
    for f in files_list:
        print("[" + str(i) + "] ID " + str(f['id']) + " " + str(f['displayName']) + "  (" + str(f['fileName']) + ")")
        i += 1

    while True:
        try:
            selected_item = files_list[int(input('> '))]
            break
        except:
            print('error: enter an valid number')

    dependencies = selected_item['dependencies']
    required_dependencies = []
    for dep in dependencies:
        if dep['relationType'] == 3:
            required_dependencies.append(dep['modId'])

    print('There are ' + str(len(required_dependencies)) + ' required dependencies for this item. Installing them too...')

    for dep in required_dependencies:
        dep_data = tools.call_curseforge_api('mods/' + str(dep))['data']
        add_once(dep_data['slug'])

    item_to_add_to_manifest['fileID'] = selected_item['id']
    item_to_add_to_manifest['filename'] = selected_item['fileName']

    print('This item is going to be added to manifest.json:')
    print()
    pprint(item_to_add_to_manifest)
    print()

    if '-y' in sys.argv:
        confirmation = 'Y'
    else:
        confirmation = input('Do you confirm that? [y/n] ').upper()
    if confirmation == 'Y' or confirmation == '':
        manifest_f = open('manifest.json', 'r')
        manifest = json.load(manifest_f)
        manifest_f.close()

        manifest['files'].append(item_to_add_to_manifest)

        manifest_f = open('manifest.json', 'w')
        manifest = json.dump(manifest, manifest_f, indent=4)
        manifest_f.close()

        print('New mod added successfully')
    else:
        print('Cancelled')


if len(sys.argv) <= 1:
    print('error: missing slugs arguments')
    sys.exit(1)


for arg in sys.argv[1:]:
    if arg != '-y':
        add_once(arg)
