from django import forms
from .models import Tag

class UploadForm(forms.Form):
	titel = forms.CharField(label='Aufgabentitel', max_length=255)
	lehrer = forms.CharField(label='Lehrer', max_length=255)
	datensatz = forms.FileField(label='Datei')
	tags = forms.ModelMultipleChoiceField(Tag)