from django.shortcuts import render
from django.http import HttpResponse

# View for the overview over the changelog
def index(request):
	return HttpResponse("Hello World")

# View for each post
def post(request, ChangelogPost_id):
	return HttpResponse("You are looking at post %s" % ChangelogPost_id)