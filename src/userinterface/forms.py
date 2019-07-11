from django import forms
from .models import Subject


class UploadForm(forms.Form):
    task_name = forms.CharField(label='Aufgabe', max_length=255)
    task_description = forms.CharField(label='Beschreibung', max_length=1000)
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Fach')
    stage = forms.ChoiceField(choices=[(stage, stage) for stage in range(1, 14)], label='Klassenstufe')
    document = forms.FileField(label='Datei hochladen')
