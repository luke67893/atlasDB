color 0A
@echo off
echo Starting dev env...
C:
XAMPP\xampp_start.exe
"Sublime Text 3\subl.exe"
D:
cd %PROJECTPATH%
start .
start cmd.exe @cmd /k "python.exe manage.py runserver"
echo Finished...