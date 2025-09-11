from django.contrib import admin
from home.models import Contact, NewsLetter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['subject', 'name', 'is_answered']
    list_editable = ['is_answered']
    list_filter = ['name', 'subject', 'is_answered']
    search_fields = ['name', 'subject']

admin.site.register(NewsLetter)
