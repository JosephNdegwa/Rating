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
def add_project(request):
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = Project(title=form.cleaned_data.get('title'),
                              photo=form.cleaned_data.get('photo'),
                              description=form.cleaned_data.get('description'),
                              link=form.cleaned_data.get('link'),
                              user=request.user)
            project.save()
            return redirect('homepage')
        else:
            return render(request, 'add-project.html', {'form': form})
    else:
        form = AddProjectForm()
        return render(request, 'add-project.html', {'form': form})

def add_rating(request, project):
    rated_project = Project.objects.get(id=project)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = Rating(design=form.cleaned_data.get('design'),
                            usability=form.cleaned_data.get('usability'),
                            content=form.cleaned_data.get('content'),
                            project=rated_project)
            rating.save()
            return redirect('homepage')
        else:
            return render(request, 'rate-project.html', {'form': form})
    else:
        form = RatingForm()
        return render(request, 'rate-project.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print("handling signup")
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.profile_photo = form.cleaned_data.get('profile_photo')
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print("signed up")
            return redirect('homepage')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})