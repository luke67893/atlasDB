# AtlasDB - Simple webtool for task sharing in schools

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
![Latest Release](https://img.shields.io/github/release/creyD/atlasDB.svg)
[![Website](https://img.shields.io/website/http/atlasdb.de.svg?down_color=red&down_message=offline&up_message=online)](http://atlasdb.de)
![Issues](https://img.shields.io/github/issues/creyD/atlasDB.svg)
![Pull Requests](https://img.shields.io/github/issues-pr/creyD/atlasDB.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6553d15548bc422497db6089a9f63f9c)](https://www.codacy.com/manual/creyD/atlasDB?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=creyD/atlasDB&amp;utm_campaign=Badge_Grade)

## Goals

:white_check_mark: Simple login system with as few as possible user groups (admins, teachers)

:white_check_mark: Folder structure with school_subjects as main folders and school_classes as sub folders

:white_check_mark: Upload feature for PDFs, Word Documents, Animations (GIF) and simple MD files

:x: Live view for Word, PDF, MD and Animations

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
