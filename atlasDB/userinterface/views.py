from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from .models import Task
from .forms import UploadForm

def welcome(request):
	if request.user.is_authenticated:
		return redirect('user_home')
	return(render(request, 'userinterface/main.html'))

def user_login(request):
	return(render(request, 'userinterface/login_form.html'))

def user_logout(request):
	return(HttpResponse("Logout Page."))

@login_required
def user_home(request):
	alltasks = Task.objects.all()
	context = {
		'tasks': alltasks
	}
	return render(request, 'userinterface/home.html', context)

@login_required
def my_tasks(request):
	my_tasks = Task.objects.filter(teacher=request.user)
	context = {
		'tasks': my_tasks
	}
	return render(request, 'userinterface/my_tasks.html', context)

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
	return render(request, 'userinterface/stageoverview.html')

@login_required
def stage(request, id):
	taskfilter = Task.objects.filter(stage=id)
	context = {
		"id": id,
		"tasks": taskfilter
	}
	return render(request, 'userinterface/stage.html', context)

@login_required
def details(request, id):
	task = Task.objects.get(id=id)
	context = {
		"task": task
	}
	return render(request, 'userinterface/details.html', context)