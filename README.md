# AtlasDB - Simple webtool for task sharing in schools :school:

## Status
:construction: :construction: :construction:

_Planning and Building_ | Testing | Finished

:construction: :construction: :construction:

## Goals

:x: Simple login system with as few as possible user groups (admins, teachers)

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

## How to get this running

### Preinstall

- Python (w. pip)
- Webbrowser
- XAMPP (MySQL-Server)

### Install

- `pip install Django==2.0.2`
- Install a MySQL-Connector for Python/ Django
- Create MySQL-Database named `atlas_db`
- Open a console window in `/taskDB/` and execute `python manage.py automigrate` to evaluate the data structure of the database
- Type `python manage.py migrate` to import the structure into your database
- To run the server type `python manage.py runserver`
--> This is just for testing but should give you a proper overview

~
