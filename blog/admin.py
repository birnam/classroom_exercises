from django.contrib import admin
from blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    fields = ['title', 'pub_date', 'body']
    list_display = ('pub_date', 'title')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    list_filter = ['pub_date']

admin.site.register(Entry, EntryAdmin)
