from django.urls import path
from . import views

urlpatterns = [
    path('', views.JournalList.as_view(), name='home'),
]
