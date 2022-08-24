from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
# from .forms import JournalForm 
# from taggit.models import Tag

# Create your views here.


class JournalList(generic.ListView):
    model = Journal
    queryset = Journal.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'


class TagList(generic.ListView):
    model = Journal
    queryset = Journal.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'

    def get_queryset(self):
        return Journal.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
