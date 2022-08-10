from django.contrib import admin
from .models import Journal

# Register your models here.


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'tags']
    prepopulated_fields = {'slug': ('author',)}
    list_filter = ('status', 'created_on')
