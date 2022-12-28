import tools


fabric_name = tools.load_manifest()['minecraft']['modLoaders'][0]['id']
fabric_version = fabric_name.split('-', 1)[-1]
print(fabric_version)
