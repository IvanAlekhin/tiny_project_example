#Tiny project example
This program do only one simple thing: returns count of ships on the text field.

##Installation
``` bash
$ git clone
```

If you're on MacOS
```$ brew install pipenv```

Or, if you're using Debian Buster+:
```$ sudo apt install pipenv```

Installation for other OS look here: https://pypi.org/project/pipenv/

Then install and activate virtualenv:

- ```$ pipenv install --dev```

- ```$ pipenv shell```

##Usage
Before this stage I assume that your virtualenv is activated (pipenv shell).

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


Run tests:
```
$ pytest tests/test_sea_battle.py
```
