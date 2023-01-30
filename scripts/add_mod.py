import tools
import sys
import pprint
import requests
import json


def add_once(slug):
    try:
        result = tools.call_curseforge_api('mods/search?gameId=' + tools.CURSEFORGE_MINECRAFT_GAME_ID + '&slug=' + slug)
        result = result['data'][0]
    except:
        print('error: invalid slug "' + slug + '"')
        return

    msg = ('Loading project ID ' + str(result['id']) + ' (' + result['slug'] + ')')
    print('=' * len(msg))
    print(msg)

    item_to_add_to_manifest = {
        "filename": "",
        "link_slug": result['slug'],
        "projectID": result['id'],
        "fileID": 0,
        "required": True,
    }

    print('Select the file you want to add to the modpack:')
    i = 0
    for f in result['latestFiles']:
        print("[" + str(i) + "] ID " + str(f['id']) + " " + str(f['displayName']) + "  (" + str(f['fileName']) + ")")
        i += 1

    while True:
        try:
            selected_item = result['latestFiles'][int(input('> '))]
            break
        except:
            print('error: enter an valid number')

    item_to_add_to_manifest['fileID'] = selected_item['id']
    item_to_add_to_manifest['filename'] = selected_item['fileName']

    print('This item is going to be added to manifest.json:')
    print()
    pprint.pprint(item_to_add_to_manifest)
    print()

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
    add_once(arg)
