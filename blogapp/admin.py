from django.contrib import admin
from .models import BlogCategory, BlogPost, BlogComments

admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(BlogComments)
