# My Fellow Dumper

My Fellow Dumper is a game dumper for Toontown Fellowship clients that run on Python 2 (aka. Clients released before October 2019). 

Clients released after October 2019 run on Python 3 and use a different build system; as such, they are not supported. 

This repository was originally hosted on a private GitLab repository. This is being made public for archival/resume reasons.

# How to Run

Clone this repository, then make sure Pipenv is installed.

Run `pipenv install` in your terminal, and wait for it to install.

Then make a folder called `gamebin` and put in your `GameData.bin` file into the folder.

Finally, run `pipenv run python src/MyFellowDumper.py` to begin the dump process.

The resulting dump will be located in a folder called `gamedump`

# License

This repository is licensed under the BSD-3-Clause license. See [this link](https://github.com/ComradeNapCali/MyFellowDumper/blob/master/LICENSE.md) for more infomation.