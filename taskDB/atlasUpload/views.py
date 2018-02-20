from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse

#from .models import Task
from .form import UploadForm

def upload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			newTask = Task(docfile=request.FILES['docfile'])
			newTask.lehrer = "Lehrer1"
			newTask.aufgabenname = "aufgabe1"
			newTask.save()
			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('upload'))
	else:
		form = UploadForm()  # A empty, unbound form
	return render(
		request,
		'atlasUpload/index.html', {'form': form}
	)

	#return render(request, 'atlasUpload/index.html')

def viewAll(request):
	# Load documents for the list page
	documents = Task.objects.all()
	return render(
		request,
		'atlasUpload/list.html', {'documents': documents, 'form': form}
	)