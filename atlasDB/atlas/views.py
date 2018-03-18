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
			return HttpResponseRedirect('errorx1/')
	else:
		form = UploadForm()
	context = {
		'title': "AtlasDB - Aufgabenerstellung",
		'form': form
	}
	return render(request, 'atlas/upload/upload.html', context)

def success(request):
	context = {
		'title': 'AtlasDB - Upload erfolgreich'
	}
	return render(request, 'atlas/upload/success.html', context)

def errorx1(request):
	context = {
		'title': 'AtlasDB - Fehler X1'
	}
	return render(request, 'atlas/upload/errorx1.html', context)

def dashboard(request):
	all_tasks = Aufgabe.objects.all()
	context = {
		'all_tasks': all_tasks,
		'title': "AtlasDB - Dashboard",
	}
	return render(request, 'atlas/dashboard.html', context)

def aufgabe(request, id):
	aufgabe = Aufgabe.objects.get(id=id)
	context = {
		'aufgabe': aufgabe,
		'title': "Aufgabe - " + aufgabe.titel,
	}
	return render(request, 'atlas/details.html', context)

def download(request, id):
	aufgabe = Aufgabe.objects.get(id=id)
	context = {
		'link': aufgabe.datensatz,
		'title': "Download - " + aufgabe.titel
	}
	return render(request, 'atlas/download.html', context)
