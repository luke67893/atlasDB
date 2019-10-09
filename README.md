<p align="center">
<h1>AtlasDB</h1>
<h3>Simple webtool for task sharing in schools</h3>

[![LICENSE](https://img.shields.io/github/license/creyD/atlasDB)](https://github.com/creyD/atlasDB/blob/master/LICENSE.md)
[![Website](https://img.shields.io/website/http/atlasdb.de.svg?down_color=red&down_message=offline&up_message=online)](http://atlasdb.de)
![Issues](https://img.shields.io/github/issues/creyD/atlasDB.svg)
![Pull Requests](https://img.shields.io/github/issues-pr/creyD/atlasDB.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6553d15548bc422497db6089a9f63f9c)](https://www.codacy.com/manual/creyD/atlasDB?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=creyD/atlasDB&amp;utm_campaign=Badge_Grade)

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
