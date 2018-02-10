# PPA 1 - Team 1

Software Testing and QA - CSE 4283 - Spring 2018

Professional Practice Assignment 1 - Team 1

## Getting Started
We are going to be working with: 

| Program                                                                     | Version |
| --------------------------------------------------------------------------- | :-----: |
| [Windows](https://www.microsoft.com/en-us/software-download/windows10)      | 10      |
| [Python](https://www.python.org/)                                           | 3.6.3   |
| [virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win) | 1.2.5   |
| [pytest](https://docs.pytest.org/en/latest/)                                | 3.4.0   |
| [pytest-html](https://pypi.python.org/pypi/pytest-html)                     | 1.16.1  |

### Install python
Download [Python 3.6.3](https://www.python.org/downloads/release/python-363/) and follow the on screen instructions leaving all of the settings as default.

### Installing and setting up virtualenv and installing requirements
We will be using a virtual environment to make things a bit easier.  Python 3 ships with 
support for this (see: `python -m venv -h`), but we are using 
[virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win) rather
than directly using the module.

**_The following steps assume you have cloned the repo and navigated to the directory that it is located it_**


``` bash
#install virtualenvwrapper-win using pip
pip install virtualenvwrapper-win

#make a new virtual environment
mkvirtualenv --python=C:\\path\\to\\python3.6\\python.exe -a C:\\path\\to\\ppa-1-sw-testing-qa-spring-2018-team-1 -r requirements.txt ppa-1

#Reference commands
#activate the virtualenv
workon ppa-1

#install requirements
pip install -r requirements.txt

#leave the virtualenv
deactivate
```

All of the requirements to run this project will be installed when you create the new virtual environment using requirements.txt

### Running Tests

To run test and generate a coverage report run the following commands in the root diretory of the repo. 

``` bash
#run test and generate html report
pytest --html=report.html --self-contained-html
```

This will automatically discover test according to [pytest's test discovery convention](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)