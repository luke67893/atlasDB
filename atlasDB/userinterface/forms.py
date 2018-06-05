from django import forms
from .models import Task, Subject

class UploadForm(forms.Form):
	task_name = forms.CharField(label='Task Title', max_length=255)	
	subject = forms.ChoiceField(choices=[(subject, subject) for subject in Subject.objects.all()])
	stage = forms.ChoiceField(choices=[(stage, stage) for stage in range(1,14)])
	document = forms.FileField(label='File')