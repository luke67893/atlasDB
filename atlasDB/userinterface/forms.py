from django.forms import ModelForm
from .models import Task, Subject

class UploadForm(ModelForm):
	class Meta:
		model = Task
		exclude = ('last_changed_at', 'uploaded_at', 'teacher')