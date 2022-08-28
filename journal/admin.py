from django.contrib import admin
from .models import Journal

# Register your models here.


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):

    list_display = ('status', 'created_on',)
    search_fields = ['author', 'tags']
    # prepopulated_fields = {'slug': ('author',)}
    list_filter = ('status', 'created_on')
