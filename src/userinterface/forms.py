from .models import Task
from django.forms import ModelForm


class UploadForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'subject', 'stage', 'document']


class UpdateTask(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'subject', 'stage', 'document']
