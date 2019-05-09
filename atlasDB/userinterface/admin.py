from django.contrib import admin

from .models import Task, Subject

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'teacher', 'subject', 'stage', 'uploaded_at')
    list_editable = ('subject', 'stage')

@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display = ('subject_id', 'subject_name')
