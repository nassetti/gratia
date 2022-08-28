from django.urls import path
from . import views

urlpatterns = [
    path('', views.JournalList.as_view(), name='home'),
    path('tags/<slug:tag_slug>/', views.TagList.as_view(), name='posts_by_tag'),
    # path('<slug:slug>/', views.JournalView.as_view(), name='journal_view'),
    path('like/<slug:tag_slug>', views.LikeInteraction.as_view(), name='journal_like'),
    # path('new_entry/', views.new_journal_entry, name='new_entry'),
    path('new_entry/', views.NewJournalEntry.as_view(), name='new_entry'),

]
