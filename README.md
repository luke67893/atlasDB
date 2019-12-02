<h1 align="center">AtlasDB</h1>
<h3 align="center">Simple webtool for task sharing for teachers</h3>

<p align="center">
<a href="https://github.com/creyD/atlasDB/blob/master/LICENSE.md"><img src="https://img.shields.io/github/license/creyD/atlasDB"></a>
<a href="http://atlasdb.de"><img src="https://img.shields.io/website/http/atlasdb.de.svg?down_color=red&down_message=offline&up_message=online"></a>
<a href="https://github.com/creyD/atlasDB/issues"><img src="https://img.shields.io/github/issues/creyD/atlasDB.svg"></a>
</p>

## Goals

:white_check_mark: Simple login system with as few as possible user groups (admins, teachers)

:white_check_mark: Folder structure with school_subjects as main folders and school_classes as sub folders

:white_check_mark: Upload feature for PDFs, Word Documents, Animations (GIF) and simple MD files

:white_check_mark: Simple search function

:white_check_mark: Tagging for documents (custom tags)


## Installation Guide

### Prerequisite

Make sure you have Python and PIP installed!

### Steps

- Clone this project and change to the folder
- Install the requirements on your system with `pip install -r requirements.txt`
- Migrate the data structure to your database using `python atlasDB/manage.py migrate`
- Create a user by typing `python atlasDB/manage.py createsuperuser`
- To run the server execute `python manage.py runserver`

--> **This is just for testing but should give you a proper overview**

## Known Issues

See [Issues](https://github.com/creyD/atlasDB/issues) tab.


Have fun!

~
