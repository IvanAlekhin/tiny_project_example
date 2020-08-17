# Tiny project example
This program do only one simple thing: returns count of ships on the text field.

## Installation
If you're on MacOS
```$ brew install pipenv```

Or, if you're using Linux:
```$ pip3 install pipenv```

If some trouble try to find info here: https://docs.pipenv.org/install/#installing-pipenv

```
$ git clone https://github.com/IvanAlekhin/tiny_project_example.git
$ cd tiny_project_example
```

Then install and activate virtualenv:

- ```$ pipenv install --dev```

- ```$ pipenv shell```

## Installation with docker
```
$ git clone https://github.com/IvanAlekhin/tiny_project_example.git
$ cd tiny_project_example
$ sudo docker build -t tiny_project .
$ sudo docker run --name sea_battle -td tiny_project
$ sudo docker exec -it sea_battle bash
```
After last step you will be in the container shell.


## Usage
Before this stage I assume that your virtualenv is activated or you are inside the docker container.

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
Other input examples you can find in test/input_examples dir.



For running tests:
```
$ pytest tests/test_sea_battle.py
```
