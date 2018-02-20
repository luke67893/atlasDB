from django import forms

class UploadForm(forms.Form):
	aufgabenname = forms.CharField(max_length=255)
	lehrer = forms.CharField(max_length=255)
	uploaddate = forms.DateTimeField()
	docfile = forms.FileField()
	