import add_mod
import sys
import json


new_minecraft_version = None
for arg in sys.argv:
    if arg.startswith('--version='):
        version_number = arg.split('--version=')[-1].strip()
        if version_number:
            new_minecraft_version = version_number


if not new_minecraft_version:
    print('error: missing argument --version=<new version>')
    sys.exit(1)


if '--full-auto' in sys.argv:
    sys.argv.append('--auto-select')
    sys.argv.append('--skip')
    sys.argv.append('-y')


manifest = add_mod.tools.load_manifest()
i = 0
while i < len(manifest['files']):
    item = manifest['files'][i]
    if item['link_slug'] in sys.argv or '--all' in sys.argv:
        new_item = add_mod.add_once(item['link_slug'], is_update=True, game_version=new_minecraft_version)
        manifest = add_mod.tools.load_manifest()
        if new_item:
            manifest['files'][i] = new_item
            manifest_f = open('manifest.json', 'w')
            json.dump(manifest, manifest_f, indent=4)
            manifest_f.close()
    i += 1


if add_mod.SKIPPED_ITEMS:
    print('========================')
    print('========================')
    print('========================')
    print('These items are skipped:')
    print('\n'.join(add_mod.SKIPPED_ITEMS))
