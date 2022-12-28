import os
import sys
import json


_VERSION_CACHE = None

BUILD_DIR = 'output'

def get_version():
    """ Loads the version name from version.txt """
    global _VERSION_CACHE
    if _VERSION_CACHE is not None:
        return _VERSION_CACHE
    version_file = open('version.txt', 'r')
    _VERSION_CACHE = version_file.read().strip()
    version_file.close()
    return get_version()


def load_manifest():
    """ Returns manifest json content """
    manifest_file = open('manifest.json', 'r')
    content = json.load(manifest_file)
    manifest_file.close()
    return content
