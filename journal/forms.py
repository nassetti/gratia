from django import forms
from django.db import models
from .models import Journal


class NewEntry(forms.ModelForm):

    # def __init__(self, **kwargs):
    #     self.author = kwargs.pop('author', None)
    #     super(NewEntry, self).__init__(**kwargs)
            
    # def save(self, commit=True):
    #     obj = super(NewEntry, self).save(commit=False)
    #     obj.author = self.author
    #     if commit:
    #         obj.save()
    #     return obj
    class Meta:
        model = Journal

        fields = [
            # 'title' ,
            # 'slug',
            # 'author',
            'one',
            'two',
            'three',
            'four',
            'five',
            'tags',
            'status',
        ]
        
