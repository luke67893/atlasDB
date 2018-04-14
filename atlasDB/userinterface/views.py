from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return(HttpResponse("Hello World."))

def login(request):
    return(HttpResponse("Login Page."))

def logout(request):
    return(HttpResponse("Logout Page."))
