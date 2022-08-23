from django.shortcuts import render
from django.views import generic
from .models import Journal
# Create your views here.


class JournalList(generic.ListView):
    model = Journal 
    queryset = Journal.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'

