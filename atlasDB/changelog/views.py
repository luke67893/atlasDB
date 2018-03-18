from django.shortcuts import render
from django.http import HttpResponse
from .models import ChangelogPost

# View for the overview over the changelog
def index(request):
	changelog = ChangelogPost.objects.all()[:10]
	context = {
		'title': 'Letzte Änderungen',
		'changelog': changelog
	}
	return render(request, 'changelog/index.html', context)
	

# View for each post
def post(request, id):
	post = ChangelogPost.objects.get(id=id)
	context = {
		'post': post
	}
	return render(request, 'changelog/posts.html', context)