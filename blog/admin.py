from django.contrib import admin
from blog.models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_date'
    search_fields = ['title', 'author']
    list_display = ['title','author','updated_date','status',]
    list_filter = ['author','updated_date','status',]
    list_editable = ['status',]

admin.site.register(Category)
