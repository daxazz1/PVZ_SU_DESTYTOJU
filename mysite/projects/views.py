from django.shortcuts import render
from django.views import generic
from .models import Project

# Create your views here.

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'project_list.html'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'project.html'