#####With development on [OmegaK2/PyPoE](https://github.com/OmegaK2/PyPoE) being discontinued, this repository was forked from [RePoE](https://github.com/brather1ng/RePoE) and exists solely to keep the [Community Wiki](https://poewiki.net) updated.


PyPoE
========

Collection of Python Tools for [Path of Exile](https://www.pathofexile.com/).

More detailed docs: [http://omegak2.net/poe/PyPoE/](http://omegak2.net/poe/PyPoE/)

The docs will be updated soon with details on how to update the specification for new leagues.


Common Problems & Advisory
--------
* Install **Python 3.7** for maximum compatibility:
* To support bundle decompression check out https://github.com/zao/ooz, compile it and place libooz.dll in the python directory
* **UI will be reworked for bundle support and is not functional at the moment**
* On Windows 10 machines there seems to a be bug in the Python installation that prevents arguments being passed to the command line interface; you can identify this issue if you get a "help" listing if you supplied more then 1 argument. See [this on stack overflow](https://stackoverflow.com/questions/2640971/windows-is-not-passing-command-line-arguments-to-python-programs-executed-from-t) for possible solutions


Overview
--------
Parts:
* Library toolkit for programmers (PyPoE/poe)
* UI based on Qt for browsing the game files (currently not working)
* CLI interface for extracting/exporting data (for the wiki, more TBD)

Resources
-------
* Discord: [Project Path of Exile Wiki](https://discord.gg/CE46HADc5T)

Important Notes
--------
Alpha Stage:
* Code structure and in particular the API may change at any time
* Incomplete in many areas (check files and TODOs)
* Tests still have to be written for a lot of things.
* Many functions and classes are not yet fully documented

Dev branch:
* Broken code may be committed occasionally to the dev branch

Installation
--------
These instructions are for the current version of PyPoE.

* [See instructions](https://github.com/Project-Path-of-Exile-Wiki/PyPoE/wiki/PyPoE-101:-Installation-and-setup)

Usage
--------
* [Exporting data for the wiki](https://github.com/Project-Path-of-Exile-Wiki/PyPoE/wiki/PyPoE-101:-Item-exporting)

Credits - People
--------
* [Grinding Gear Games](http://www.grindinggear.com/) - they created many of the file formats and [Path of Exile](https://www.pathofexile.com/) obviously, so do not reuse their files anywhere without their permission and support them if you are able to :)
* [OmegaK2](https://github.com/OmegaK2) - Original developer of PyPoE
* [brather1ng](https://github.com/brather1ng) - For the updated fork
* [Chriskang](http://pathofexile.gamepedia.com/User:Chriskang) and the original [VisualGGPK2](http://pathofexile.gamepedia.com/User:Chriskang/VisualGGPK2)
* [chuanhsing](https://www.reddit.com/u/chuanhsing) ([poedb](http://poedb.tw/us/index.php)) for helping with meaning of certain specification values and retrieving monster stats

Credits - Libraries
-------
* [pyside2](https://wiki.qt.io/Qt_for_Python) ([pypi](https://pypi.org/project/PySide2/))
* [configobj](http://www.voidspace.org.uk/python/configobj.html) ([pypi](https://pypi.org/project/configobj/))
* colorama ([pypi](https://pypi.org/project/colorama/))
* sphinx ([pypi](https://pypi.org/project/sphinx/))
* pytest ([pypi](https://pypi.org/project/pytest/))
* PyOpenGL ([pypi](https://pypi.org/project/PyOpenGL/))
* tqdm ([pypi](https://pypi.org/project/tqdm/))
* graphviz ([pypi](https://pypi.org/project/graphviz/))
* mwclient ([pypi](https://pypi.org/project/mwclient/))
* mwclientparserfromhell ([pypi](https://pypi.org/project/mwparserfromhell/))
* rapidfuzz ([pypi](https://pypi.org/project/rapidfuzz/))
