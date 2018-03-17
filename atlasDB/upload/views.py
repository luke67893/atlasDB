from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import staticfiles

from .models import Aufgabe
from .forms import UploadForm

def upload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			newTask = Aufgabe(titel=request.POST['titel'], lehrer=request.POST['lehrer'], tags=request.POST['tags'], datensatz=request.FILES['datensatz'])
			newTask.save()
			return HttpResponseRedirect('success/')
	else:
		form = UploadForm()
	return render(request, 'upload/upload.html', {'form': form})

def success(request):
	return render(request, 'upload/success.html')
