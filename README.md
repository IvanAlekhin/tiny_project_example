# Tiny project example
This program do only one simple thing: returns count of ships on the text field.

## Installation
``` bash
$ git clone https://github.com/IvanAlekhin/tiny_project_example.git
```

If you're on MacOS
```$ brew install pipenv```

Or, if you're using Debian Buster+:
```$ sudo apt install pipenv```

Installation for other OS look here: https://pypi.org/project/pipenv/

Then install and activate virtualenv:

- ```$ pipenv install --dev```

- ```$ pipenv shell```

## Usage
Before this stage I assume that your virtualenv is activated.

Run with your own file:
```
$ python3 main.py --file your/absolute/path/to/file.txt
```
where file.txt is something like
```
#---------
#------###
#-----#---
#-----#---
------#---
---##-----
----------
----------
-----####-
----------
```
After scanning this file, program returns 5.  It is number of ships in the text field.



For running tests:
```
$ pytest tests/test_sea_battle.py
```
