from django.contrib import admin
from blog.models import *
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'updated_date'
    search_fields = ['title', 'author']
    list_display = ['title','author','updated_date','status',]
    list_filter = ['author','updated_date','status',]
    list_editable = ['status',]
    summernote_fields = ['content',]

admin.site.register(Category)
