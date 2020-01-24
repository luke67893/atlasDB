<h1 align="center">AtlasDB</h1>
<h3 align="center">Webtool for task sharing for teachers</h3>

[![CodeFactor](https://www.codefactor.io/repository/github/creyd/prettier_action/badge/master)](https://www.codefactor.io/repository/github/creyd/prettier_action/overview/master)
[![License](https://img.shields.io/github/license/creyD/atlasDB)](https://github.com/creyD/atlasDB/blob/master/LICENSE.md)
[![Website](https://img.shields.io/website/http/atlasdb.de.svg?down_color=red&down_message=offline&up_message=online)](https://atlasdb.de)
[![Issues](https://img.shields.io/github/issues/creyD/atlasDB.svg)](https://github.com/creyD/atlasDB/issues)

## Goals

:white_check_mark: Simple login system with as few as possible user groups (admins, teachers)

:white_check_mark: Folder structure with school_subjects as main folders and school_classes as sub folders

:white_check_mark: Upload feature for PDFs, Word Documents, Animations (GIF) and simple MD files

:white_check_mark: Simple search function

:white_check_mark: Tagging for documents (custom tags)


## Installation Guide

- Install [Python 3](https://www.python.org/) and PIP
- Clone this project
- Install the requirements on your system with `pip install -r requirements.txt`
- Migrate the data structure to your database using `python manage.py migrate`
- Create a user by typing `python manage.py createsuperuser`
- To run the server execute `python manage.py runserver`

--> **This is just for testing but should give you a proper overview**

## Known Issues

See [Issues](https://github.com/creyD/atlasDB/issues) tab.


Have fun!

~
