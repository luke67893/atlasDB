from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from .models import Task
from .forms import UploadForm

def welcome(request):
	if request.user.is_authenticated:
		return redirect('user_home')
	context = {
		'ptitle': "Welcome to atlasDB"
	}
	return render(request, 'userinterface/main.html', context)

def user_login(request):
	context = {
		'ptitle': "Login"
	}
	return render(request, 'userinterface/login_form.html', context)

def user_logout(request):
	return HttpResponse("Logout Page.")

@login_required
def user_home(request):
	alltasks = Task.objects.all()
	context = {
		'headline': "All tasks",
		'tasks': alltasks,
		'ptitle': "Home - " + request.user.username
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def my_tasks(request):
	my_tasks = Task.objects.filter(teacher=request.user)
	context = {
		'headline': "Your tasks (" + request.user.username + ")",
		'tasks': my_tasks,
		'ptitle': "My Tasks"
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
	return render(request, 'userinterface/upload.html', { 'form': form })

@login_required
def stages(request):
	context = {
		'ptitle': "Stageoverview"
	}
	return render(request, 'userinterface/stageoverview.html', context)

@login_required
def stage(request, id):
	taskfilter = Task.objects.filter(stage=id)
	context = {
		'id': id,
		'tasks': taskfilter,
		'headline': "Stage " + str(id),
		'ptitle': "Stage " + str(id)
	}
	return render(request, 'userinterface/taskview.html', context)

@login_required
def details(request, id):
	task = Task.objects.get(id=id)
	context = {
		'task': task,
		'ptitle': "Task - " + task.task_name
	}
	return render(request, 'userinterface/details.html', context)