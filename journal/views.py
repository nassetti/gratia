from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import NewEntry
from .models import Journal
# from taggit.models import Tag

# Create your views here.


class JournalList(generic.ListView):
    model = Journal
    queryset = Journal.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'


class AuthorList(generic.ListView):
    model = Journal
    queryset = Journal.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'

    def get_queryset(self):
        return Journal.objects.filter(author=self)


# class YourEntries(generic.ListView):
#     model = Journal
#     queryset = Journal.objects.filter(status=1).order_by('-created_on')
#     template_name = 'your-entries.html'

#     def get_queryset(self):
#         return Journal.objects.filter(author=)


class TagList(generic.ListView):
    model = Journal
    queryset = Journal.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'

    def get_queryset(self):
        return Journal.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


# class JournalView(View):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Journal.objects.filter(status=1)
#         journal = get_object_or_404(queryset, slug=slug)
#         liked = False
#         if journal.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             'journal-view.html',
#             {
#                 'journal': journal,
#                 'liked': liked
#             },
#         )   


class LikeInteraction(View):

    def journal(self, request, slug):
        journal = get_object_or_404(Journal, slug=slug)

        if journal.likes.filter(id=request.user.id).exists():
            journal.likes.remove(request.user)
        else:
            journal.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('home'), args=[slug])


class NewJournalEntry(FormView):
    template_name = 'journal-entry.html'
    form_class = NewEntry
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

