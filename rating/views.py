from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import *
from .forms import SignUpForm, AddProjectForm, RatingForm
from .models import Project, Rating
from django.contrib.auth import logout

def homepage(request):
    projects = Project.objects.all()
    return render(request, "homepage.html", {"projects": projects})

def profile(request):
    projects = Project.objects.filter(user=request.user)
    print(projects)
    return render(request, "profile.html", {"projects": projects})

def project(request, project):
    current_project = Project.objects.get(id=project)
    return render(request, "project.html", {"project": current_project})

def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.objects.filter(title__icontains=search_term)
        #return render(request, 'search.html',{"search_term": search_term,"searched_usernames": searched_usernames})
        print(search_term)
        return render(request, 'search.html', {"search_term": search_term, "projects": searched_projects})
    else:
        message = "No Results"
        return render(request, 'search.html', {"message":message})
