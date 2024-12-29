from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):    
    prepopulated_fields = { 'slug' : ('title',), }
    list_display = ['title', 'author', 'created_on',]
    
admin.site.register(Blog, BlogAdmin)