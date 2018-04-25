from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from .models import Task

def welcome(request):
	if request.user.is_authenticated:
		return redirect('user_home')
	return(render(request, 'userinterface/main_template.html'))

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