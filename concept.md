# Concept for AtlasDB - DRAFT

## Views:
- Upload Form
  - Name of Task (Textfield)
  - Teacher (Automatically)
  - Document
  - Subject Dropdown Menu
  - Stage Dropdown Menu
  - Tag Adder
- Dashboards
  - All tasks/ Activity Overview
  - Search function
  - Sort by tags, teachers
  - Folder Structure Views (Stage > Subject)
- Login Page
- Logout Page
- Welcome Page (no login required)
- Admin Views
  - Add subjects
  - Add stages
  - Add tags

## Models:
- Tasks
  - Teacher (ForeignKey)
  - UploadDate (AutoNow)
  - LastChanged (AutoUpdate)
  - TaskName (CharField)
  - Document (docfile)
  - Stage (Integer Range 1 - 13)
  - Subject (ForeignKey)
- Teachers (Django.Users)
- Subjects
  - SubjectName
- Tags
  - TagName
  - TagColor (hexadecimal)
