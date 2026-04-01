from django.shortcuts import render
from .models import Project, Skill, Education

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def education(request):
    education = Education.objects.all()
    return render(request, 'portfolio/education.html', {'education': education})

def contact(request):
    return render(request, 'portfolio/contact.html')