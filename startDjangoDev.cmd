@echo off
color 0A

set pathproject=D:\Development\project_atlasDB\atlasDB
set pathxampp=C:\XAMPP\

echo Starting dev env...
C:
cd %pathxampp%
xampp_start.exe
"Sublime Text 3\subl.exe"
D:
cd %pathproject%
start .
start cmd.exe @cmd /k "python.exe manage.py runserver"
echo Finished...
