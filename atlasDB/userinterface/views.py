from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from .models import Task, Subject
from .forms import UploadForm

# For downloads
import os
from django.conf import settings

def user_logout(request):
	return HttpResponse("Logout Page.")

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

def help(request):
	context = {
		'ptitle': "Help",
		'pheadline': "Help for atlasDB"
	}
	return render(request, 'userinterface/help.html', context)

def impressum(request):
	context = {
		'ptitle': "Impressum",
		'pheadline': "Impressum"
	}
	return render(request, 'userinterface/impressum.html', context)

@login_required
def user_home(request):
	context = {
		'tasks': Task.objects.all(),
		'ptitle': "Home - " + request.user.username,
		'pheadline': "All tasks"
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def my_tasks(request):
	my_tasks = Task.objects.filter(teacher=request.user)
	context = {
		'tasks': my_tasks,
		'tasknumber': len(my_tasks),
		'ptitle': "My Tasks",
		'pheadline': "Your tasks (" + request.user.username + ")"
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def upload(request):
	if request.method == "POST":
		new_task = Task(teacher=request.user, task_name=request.POST['task_name'], subject=Subject.objects.get(subject_name=request.POST['subject']), stage=request.POST['stage'], document=request.FILES['document'])
		new_task.save()
		return redirect('user_home')
	context = {
		'form': UploadForm(),
		'ptitle': "Upload",
		'pheadline': "Upload"
	}
	return render(request, 'userinterface/upload.html', context)

@login_required
def searchoverview(request):
	context = {
		'ptitle': "Search",
		'pheadline': "Search a task"
	}
	return render(request, 'userinterface/searchbar.html', context)

@login_required
def search(request, keyword):
	results = Task.objects.filter(task_name__contains=keyword)
	if len(results)==0:
		raise Http404("No tasks found.")
	context = {
		'ptitle': "Search: " + str(keyword),
		'pheadline': "Search: " + str(keyword),
		'tasks': results
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def stages(request):
	stages = []
	[ stages.append(i) for i in range(1,14) ]
	context = {
		'ptitle': "Stage Overview",
		'pheadline': "All stages",
		'stages': stages
	}
	return render(request, 'userinterface/overview.html', context)

@login_required
def stage(request, stagenumber):
	taskfilter = Task.objects.filter(stage=stagenumber) 
	context = {
		'stage': stagenumber,
		'tasks': taskfilter,
		'ptitle': "Filter: Stage " + str(stagenumber),
		'pheadline': "Filter: Stage " + str(stagenumber),
		'subjects': Subject.objects.all(),
		'tasknumber': len(taskfilter)
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def subjects(request):
	context = {
		'ptitle': "Subject Overview",
		'pheadline': "All subjects",
		'subjects': Subject.objects.all()
	}
	return render(request, 'userinterface/overview.html', context)

@login_required
def subject(request, subject):
	subject_id, taskfilter = Subject.objects.get(subject_name=subject), Task.objects.filter(subject_id=subject_id)
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
	context = {
		'task': task,
		'ptitle': "Task - " + task.task_name,
		'pheadline': "Task " + task.task_name,
		'owner': [ 1 if str(task.teacher) == str(request.user.username) else 0 ]
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