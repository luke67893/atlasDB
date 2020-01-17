from django.contrib import admin
from .models import Task, Subject, Tag, TaskTags


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'teacher', 'subject', 'stage', 'uploaded_at', 'task_description')
    list_editable = ('subject', 'stage')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'subject_name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'tag_name', 'tag_color')


@admin.register(TaskTags)
class TaskTagConnector(admin.ModelAdmin):
    list_display = ('task', 'tag')
