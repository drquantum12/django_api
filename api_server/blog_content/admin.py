from django.contrib import admin
from .models import blog_content
# Register your models here.

admin.site.register(blog_content)

# for much more flexible access

# @admin.register(Book)
#class BookAdmin(admin.ModelAdmin):
#  fields = ['title', 'date_updated']           example fields that we want to view
# or list_display = ['title', 'date_updated']   both do same work
# or 'list_filter' for list filtering
# or  'search_filter'
