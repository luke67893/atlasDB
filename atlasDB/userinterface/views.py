from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import Task, Subject
from .forms import UploadForm

# For downloads
import os
from django.conf import settings


def user_logout(request):
    return HttpResponse('Logout Page.')


def welcome(request):
    if request.user.is_authenticated:
        return redirect('user_home')
    context = {
        'ptitle': 'Welcome to atlasDB',
        'pheadline': ''
    }
    return render(request, 'userinterface/main.html', context)


def user_login(request):
    context = {
        'ptitle': 'Login to atlasDB',
        'pheadline': 'Login to atlasDB'
    }
    return render(request, 'userinterface/login_form.html', context)


def help(request):
    context = {
        'ptitle': 'Help',
        'pheadline': 'Help for atlasDB'
    }
    return render(request, 'userinterface/help.html', context)


def impressum(request):
    context = {
        'ptitle': 'Impressum',
        'pheadline': 'Impressum'
    }
    return render(request, 'userinterface/impressum.html', context)


@login_required
def user_home(request):
    context = {
        'tasks': Task.objects.all(),
        'ptitle': 'Home - ' + request.user.username,
        'pheadline': 'All tasks'
    }
    return render(request, 'userinterface/taskview.html', context)


@login_required
def my_tasks(request):
    my_tasks = Task.objects.filter(teacher=request.user)
    context = {
        'tasks': my_tasks,
        'tasknumber': len(my_tasks),
        'ptitle': 'My Tasks',
        'pheadline': 'Your tasks (' + request.user.username + ')'
    }
    return render(request, 'userinterface/taskview.html', context)


@login_required
def upload(request):
    form = UploadForm()

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            Task.objects.get_or_create(
                teacher=request.user,
                task_name=form.cleaned_data['task_name'],
                subject=form.cleaned_data['subject'],
                stage=form.cleaned_data['stage'],
                document=request.FILES['document']
            )
            return redirect('user_home')

    context = {
        'form': form,
        'ptitle': 'Upload',
        'pheadline': 'Upload'
    }
    return render(request, 'userinterface/upload.html', context)


@login_required
def searchoverview(request):
    context = {
        'ptitle': 'Search',
        'pheadline': 'Search a task'
    }
    return render(request, 'userinterface/searchbar.html', context)


@login_required
def search(request, keyword):
    results = Task.objects.filter(task_name__contains=keyword)
    if len(results) == 0:
        raise Http404('No tasks found.')
    context = {
        'ptitle': 'Search: ' + str(keyword),
        'pheadline': 'Search: ' + str(keyword),
        'tasks': results
    }
    return render(request, 'userinterface/taskview.html', context)


@login_required
def stages(request):
    context = {
        'ptitle': 'Stage Overview',
        'pheadline': 'All stages',
        'stages': range(1, 14)
    }
    return render(request, 'userinterface/overview.html', context)


@login_required
def stage(request, stagenumber):
    taskfilter = Task.objects.filter(stage=int(stagenumber))
    context = {
        'stage': stagenumber,
        'tasks': taskfilter,
        'ptitle': 'Filter: Stage ' + str(stagenumber),
        'pheadline': 'Filter: Stage ' + str(stagenumber),
        'subjects': Subject.objects.all(),
        'tasknumber': len(taskfilter)
    }
    return render(request, 'userinterface/taskview.html', context)


@login_required
def subjects(request):
    context = {
        'ptitle': 'Subject Overview',
        'pheadline': 'All subjects',
        'subjects': Subject.objects.all()
    }
    return render(request, 'userinterface/overview.html', context)


@login_required
def subject(request, subjectid):
    subject = Subject.objects.get(subject_id=subjectid)
    taskfilter = Task.objects.filter(subject=subject)

    context = {
        'subject': subject.subject_name,
        'tasks': taskfilter,
        'ptitle': 'Filter: Subject ' + subject.subject_name,
        'pheadline': 'Filter: Subject ' + subject.subject_name,
        'tasknumber': len(taskfilter)
    }

    return render(request, 'userinterface/taskview.html', context)


@login_required
def stagesubject(request, stagenumber, subjectid):
    subject = Subject.objects.get(subject_id=subjectid)
    taskfilter = Task.objects.filter(stage=stagenumber, subject_id=subject)

    context = {
        'subject': subject.subject_name,
        'tasks': taskfilter,
        'ptitle': 'Filter: Stage ' + str(stagenumber) + ' and subject ' + subject.subject_name,
        'pheadline': 'Filter: Stage ' + str(stagenumber) + ' and subject ' + subject.subject_name,
        'tasknumber': len(taskfilter)
    }

    return render(request, 'userinterface/taskview.html', context)


@login_required
def details(request, taskid):
    task = Task.objects.get(task_id=taskid)

    context = {
        'task': task,
        'ptitle': 'Task - ' + task.task_name,
        'pheadline': 'Task ' + task.task_name,
        'owner': [True if str(task.teacher) == str(request.user.username) else False]
    }

    return render(request, 'userinterface/details.html', context)


@login_required
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404('File does not exist.')
