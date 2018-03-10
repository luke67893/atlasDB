from django.shortcuts import render
from django.http import HttpResponse

from upload.models import Aufgabe

def dashboard(request):
	all_tasks = Aufgabe.objects.all()
	context = {
		'all_tasks': all_tasks
	}
	return render(request, 'dashboard/layout.html', context)

def aufgabe(request, id):
	aufgabe = Aufgabe.objects.get(id=id)
	context = {
		'aufgabe': aufgabe
	}
	return render(request, 'dashboard/details.html', context) 