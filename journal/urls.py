from django.urls import path
from . import views

urlpatterns = [
    path('', views.JournalList.as_view(), name='home'),
    path('tags/<slug:tag_slug>/', views.TagList.as_view(), name='posts_by_tag'),

]
