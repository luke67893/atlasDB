from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import staticfiles

from .models import Aufgabe
from .forms import UploadForm

def upload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			newTask = Aufgabe(titel=request.POST['titel'], lehrer=request.POST['lehrer'], datensatz=request.FILES['datensatz'])
			# Insert in line above tags=request.POST['tags'], 
			newTask.save()
			return HttpResponseRedirect('success/')
		else:
			return HttpResponseRedirect('error/')
	else:
		form = UploadForm()
	return render(request, 'atlas/upload/upload.html', {'form': form})

def success(request):
	return render(request, 'atlas/upload/success.html')

def error(request):
	return render(request, 'atlas/upload/error.html')

def dashboard(request):
	all_tasks = Aufgabe.objects.all()
	context = {
		'all_tasks': all_tasks
	}
	return render(request, 'atlas/layout.html', context)

def aufgabe(request, id):
	aufgabe = Aufgabe.objects.get(id=id)
	context = {
		'aufgabe': aufgabe
	}
	return render(request, 'atlas/details.html', context)