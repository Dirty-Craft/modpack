import os
import sys
import json


_VERSION_CACHE = None

BUILD_DIR = '_build'

CURSEFORGE_URL = 'https://api.curseforge.com/v1/'
CURSEFORGE_MINECRAFT_GAME_ID = '432'
CURSEFORGE_MINECRAFT_MODS_CLASS_ID = '6'

def get_version():
    """ Loads the version name from version.txt """
    global _VERSION_CACHE
    if _VERSION_CACHE is not None:
        return _VERSION_CACHE
    version_file = open('version.txt', 'r')
    _VERSION_CACHE = version_file.read().strip()
    version_file.close()
    return get_version()


def get_game_version():
    return load_manifest()['minecraft']['version']


def load_manifest():
    """ Returns manifest json content """
    manifest_file = open('manifest.json', 'r')
    content = json.load(manifest_file)
    manifest_file.close()
    return content


def get_curseforge_api_key():
    api_key_file = open('.curseforge-api-key.txt', 'r')
    api_key = api_key_file.read().strip()
    api_key_file.close()
    return api_key


def call_curseforge_api(path, method="GET", data={}):
    import requests
    api_key = get_curseforge_api_key()
    headers = {
        'x-api-key': api_key,
        'Accept': 'application/json',
    }
    method = method.upper()
    action = requests.get
    url = CURSEFORGE_URL + path
    if method == 'POST':
        action = requests.post
    return json.loads(action(url, headers=headers, data=data).text)
