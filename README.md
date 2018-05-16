# AtlasDB - Simple webtool for task sharing in schools

## Status
:construction: :construction: :construction:

Planning | _Building_ | Testing | Finished

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

:construction: :construction: :construction:

## Goals

:white_check_mark: Simple login system with as few as possible user groups (admins, teachers)

:x: Folder structure with school_subjects as main folders and school_classes as sub folders

:x: Upload feature for PDFs, Word Documents, Animations (GIF) and simple MD files

:x: Live view for Word, PDF, MD and Animations

:x: Simple search function (by tags and by users)

:x: Tagging for documents (custom tags)

:x: Detailed information for documents on hover


## Technology

- Language: Django (Python, HTML, JS, CSS)
- Database: MySQL (later)
- Webserver:  Apache

## Install Guide

### Preinstall

- Python (w/ pip)
- Webbrowser
- XAMPP (MySQL-Server)

### Install

- `pip install Django==2.0.2`
- Install a MySQL-Connector for Python/ Django
- Create MySQL-Database named `atlas_db`
- Open a console window in `/atlasDB/` and execute `python manage.py makemigrations` to evaluate the data structure of the database
- Type `python manage.py migrate` to import the structure into your database
- To run the server type `python manage.py runserver`

--> This is just for testing but should give you a proper overview

~
