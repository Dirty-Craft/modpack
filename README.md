# Dirty Craft - A Minecraft modpack
The Dirty Craft is a Fabric modpack for Minecraft.

Check this out on [Curseforge](https://www.curseforge.com/minecraft/modpacks/dirty_craft/).

Dirty craft is a modpack which inclues different mods to make MineCraft more realistic in overworld.
It adds more crops, fruits, animals, etc.

In addition to more nature and realistic, it also adds more monsters, boss fights, and mysterious structures.

Also if you are bored from the current look of End and Nether dimentions, it adds better nether & end.

And the Blumbzone dimention is added too.

Totally, if you want to experience a MineCraft with **More content**, this will be the best thing to try!

Also we have lots of plans in future for this modpack!

## Mods
To see list of the available mods in this modpack, see [mods list](MODS.md).

## Using this repository & Contribution
If you are interested in collaborating to this project,
Here's for you.

This project is self-documented.

We do everything automatically using **Makefile**.
Check [here](HOW-TO-USE-MAKEFILE.md) to see the available commands.

#### How to add & update mods
To do this, you have to edit [manifest.json](manifest.json)
and change `fileID` value or add a new mod.
If you wanna add a new mod, don't forget to set `filename` and `slug` keys too.
They are used in scripts.

#### How to change Minecraft folder config & other files
You can do it by adding whatever you want in `overrides` folder.

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

#### How to generate the modpack for server side
To generate the server modpack:

```shell
$ make server
```

It will be generated as a zip file in `_build/server` as a zip file.

## License
This project is created by [parsampsh](https://github.com/parsampsh) and other contributors.
And it's licensed under [MIT License](LICENSE).
