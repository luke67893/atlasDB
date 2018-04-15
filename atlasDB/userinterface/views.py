from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Task

def welcome(request):
    return(render(request, 'userinterface/main_template.html'))

def login(request):
    return(render(request, 'userinterface/login_form.html'))

def logout(request):
    return(HttpResponse("Logout Page."))

@login_required
def main(request):
    # my_tasks = Task.objects.all()
    return(HttpResponse("Shouldnt see this"))
