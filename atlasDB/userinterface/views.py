from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from .models import Task, Subject
from .forms import UploadForm

# For downloads
import os
from django.conf import settings

def welcome(request):
	if request.user.is_authenticated:
		return redirect('user_home')
	context = {
		'ptitle': "Welcome to atlasDB",
		'pheadline': "Hi there!"
	}
	return render(request, 'userinterface/main.html', context)

def user_login(request):
	context = {
		'ptitle': "Login to atlasDB",
		'pheadline': "Login to atlasDB"
	}
	return render(request, 'userinterface/login_form.html', context)

def user_logout(request):
	return HttpResponse("Logout Page.")

@login_required
def user_home(request):
	alltasks = Task.objects.all()
	context = {
		'tasks': alltasks,
		'ptitle': "Home - " + request.user.username,
		'pheadline': "All tasks"
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def my_tasks(request):
	my_tasks = Task.objects.filter(teacher=request.user)
	tasknumber = len(my_tasks)
	context = {
		'tasks': my_tasks,
		'tasknumber': tasknumber,
		'ptitle': "My Tasks",
		'pheadline': "Your tasks (" + request.user.username + ")"
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def upload(request):
	if request.method == "POST":
		new_task = Task(teacher=request.user)
		form = UploadForm(instance=new_task, data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('user_home')
	else:
		form = UploadForm()
	context = {
		'form': form,
		'ptitle': "Upload",
		'pheadline': "Upload"
	}
	return render(request, 'userinterface/upload.html', context)

@login_required
def stages(request):
	context = {
		'ptitle': "Stage Overview",
		'pheadline': "All stages"
	}
	return render(request, 'userinterface/stageoverview.html', context)

@login_required
def stage(request, stagenumber):
	subjects = Subject.objects.all()
	taskfilter = Task.objects.filter(stage=stagenumber)
	context = {
		'stage': stagenumber,
		'tasks': taskfilter,
		'ptitle': "Filter: Stage " + str(stagenumber),
		'pheadline': "Filter: Stage " + str(stagenumber),
		'subjects': subjects,
		'tasknumber': len(taskfilter)
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def subjects(request):
	subjects = Subject.objects.all()
	context = {
		'ptitle': "Subject Overview",
		'pheadline': "All subjects",
		'subjects': subjects
	}
	return render(request, 'userinterface/overview.html', context)

@login_required
def subject(request, subject):
	subject_id = Subject.objects.get(subject_name=subject)
	taskfilter = Task.objects.filter(subject_id=subject_id)
	context = {
		'subject': subject,
		'tasks': taskfilter,
		'ptitle': "Filter: Subject " + subject,
		'pheadline': "Filter: Subject " + subject,
		'tasknumber': len(taskfilter)
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def stagesubject(request, stagenumber, subject):
	subject_id = Subject.objects.get(subject_name=subject)
	taskfilter = Task.objects.filter(stage=stagenumber, subject_id=subject_id)
	context = {
		'subject': subject,
		'tasks': taskfilter,
		'ptitle': "Filter: Stage " + str(stagenumber) + " and subject " + subject,
		'pheadline': "Filter: Stage " + str(stagenumber) + " and subject " + subject,
		'tasknumber': len(taskfilter)
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def details(request, id):
	task = Task.objects.get(id=id)
	owner = 0
	if str(task.teacher) == str(request.user.username):
		owner = 1
	context = {
		'task': task,
		'ptitle': "Task - " + task.task_name,
		'pheadline': "Task " + task.task_name,
		'owner': owner
	}
	return render(request, 'userinterface/details.html', context)

@login_required
def download(request, path):
	file_path = os.path.join(settings.MEDIA_ROOT, path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as file:
			response = HttpResponse(file.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404("File does not exist.")