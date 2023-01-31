# Dirty Craft - A Minecraft modpack
The Dirty Craft is a Fabric modpack for Minecraft.

Check this out on [Curseforge](https://www.curseforge.com/minecraft/modpacks/dirty_craft/).

Dirty craft is a modpack which includes different mods to make MineCraft more realistic in overworld.
It adds more crops, fruits, animals, etc.

In addition to more nature and realisticness, it also adds more monsters, boss fights, and mysterious structures.

Also if you are bored from the current look of End and Nether dimentions, it adds better nether & end.

And the Blumbzone dimention is added too.

Totally, if you want to experience a MineCraft with **More content**, this will be the best thing to try!

Also we have lots of plans in the future for this modpack!

## Mods
To see list of the available mods in this modpack, see [mods list](MODS.md).

## Using this repository & Contribution
If you are interested in collaborating to this project,
Here's for you.

We do everything automatically using **Makefile** (which is self-documented).
Check [here](HOW-TO-USE-MAKEFILE.md) to see the available commands.

#### How to add & update mods
To do this, you should edit [manifest.json](manifest.json)
and change `fileID` value or add a new mod.
If you wanna add or update mods, don't forget to set `filename` and `slug` keys too.
They are used in scripts.

**Looking for an easier way to add mods?** Use the automated script:

```shell
$ python3 scripts/add_mod.py <slugs...>
$ python3 scripts/add_mod.py betterend the-bumblezone-fabric
$ python3 scripts/add_mod.py betterend the-bumblezone-fabric -y # you can use -y flag to skip the confirmation step
$ python3 scripts/add_mod.py betterend the-bumblezone-fabric --auto-select # you can also automate the file selection. but some times it fails to do it, so it may ask you to do it manually for some items
$ python3 scripts/add_mod.py betterend the-bumblezone-fabric --auto-select --skip # if you want to skip the ones that their version can't be selected automatically, you can use --skip. It skips them and prints them at the end of the process, so you can try to add them again later
$ python3 scripts/add_mod.py betterend the-bumblezone-fabric --auto-select --skip -y # and this will be the most automated mode for it
$ python3 scripts/add_mod.py betterend the-bumblezone-fabric --full-auto # or you can use --full-auto, it equals `--auto-select --skip -y`
```

Then you should select the file that you want to be selected, then it will be added to the manifest.json!

**NOTE**: to use this script, you need to create a file called `.curseforge-api-key.txt` and put **Curseforge API key** in it.
And it also requires **Python `requests` package** too.

#### How to change Minecraft folder config & other files
You can do it by adding whatever you want in `overrides` folder (for example `overrides/config` folder to override configs).

#### How to download mods on my local
To do that:

```shell
$ make mods
```

They all will be downloaded and cached in `_build/mods/jar`
and also a compressed version will be created in `_build/mods/zip`.

#### How to generate modpack file
To do that:

```shell
$ make modpack
```

It will be generated as a zip file in `_build/modpack`.
This file can be uploaded to the Curseforge and installed by players.

#### How to generate the modpack for server side
To generate the server modpack:

```shell
$ make server
```

It will be generated as a zip file in `_build/server` as a zip file.

#### What to do by the way?
We write our TODOs & plans in [TODO.md](TODO.md). Check it out.

#### How to publish this to Curseforge?
The project will be automatically published to the Curseforge when you add a **tag**.
See [Publish workflow](.github/workflows/publish.yml) if you are interested.

## License
This project is created by [parsampsh](https://github.com/parsampsh) and other contributors.
And it's licensed under [MIT License](LICENSE).
