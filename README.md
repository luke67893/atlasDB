# AtlasDB - Simple webtool for task sharing in schools

## Status
:construction: :construction: :construction:

Planning | _Building_ | Testing | Finished

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

:construction: :construction: :construction:

## Goals

:white_check_mark: Simple login system with as few as possible user groups (admins, teachers)

:white_check_mark: Folder structure with school_subjects as main folders and school_classes as sub folders

:white_check_mark: Upload feature for PDFs, Word Documents, Animations (GIF) and simple MD files

:x: Live view for Word, PDF, MD and Animations

:x: Simple search function (by tags and by users)

:x: Tagging for documents (custom tags)


## Technology

- Language: Django (Python, HTML, JS, CSS)
- Database: MySQL
- Webserver: Apache (later)

## Install Guide

### Preinstall

- Python (w/ pip)
- Database (XAMPP, MySQL Server...)

### Install testing environment

- `pip install Django==2.0.2`
- Install a DB connector for Django (i.e. `pip install mysql-python`)
- Clone this project (`git clone https://bitbucket.org/creyd/project_atlasdb` or in SourceTree)
- Create superusers and users
- Adjust database connector in `settings.py`
- Open a console window in `/atlasDB/` and execute `python manage.py makemigrations` and `python manage.py migrate` to migrate data structure to the database
- Adjust help site in `templates/userinterface/help.html` and impressum under `templates/userinterface/impressum.html` and main site (welcome site) under `templates/userinterface/main.html`
- Adjust bottom line watermark (YOUR COMPANY NAME) in `main_temlate.html`
- Add your custom favicon in `/atlasDB/userinterface/static/userinterface`
- To run the server type `python manage.py runserver`

Have fun adjusting your own version

--> **This is just for testing but should give you a proper overview**

~
