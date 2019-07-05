[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
![Latest Release](https://img.shields.io/github/release/creyD/atlasDB.svg)
[![Website](https://img.shields.io/website/http/atlasdb.de.svg?down_color=red&down_message=offline&up_message=online)](http://atlasdb.de)
![Issues](https://img.shields.io/github/issues/creyD/atlasDB.svg)
![Pull Requests](https://img.shields.io/github/issues-pr/creyD/atlasDB.svg)
# AtlasDB - Simple webtool for task sharing in schools

:construction: :construction: :construction:

Planning | Building | _Testing_ | Finished

## Goals

:white_check_mark: Simple login system with as few as possible user groups (admins, teachers)

:white_check_mark: Folder structure with school_subjects as main folders and school_classes as sub folders

:white_check_mark: Upload feature for PDFs, Word Documents, Animations (GIF) and simple MD files

:x: Live view for Word, PDF, MD and Animations

:white_check_mark: Simple search function

:x: Tagging for documents (custom tags)


## Technology

- Python 3
- Django

## Installation Guide

- Clone this project and change to the folder
- `pip install -r requirements.txt`
- Open a console window and execute `python atlasDB/manage.py migrate`
- Create a user by typing `python atlasDB/manage.py createsuperuser`
- To run the server type `python manage.py runserver`

--> **This is just for testing but should give you a proper overview**

Have fun adjusting your own version

## Known Issues

See [Issues](https://github.com/creyD/atlasDB/issues) tab.
