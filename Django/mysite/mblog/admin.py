from email.headerregistry import Address
import imp
from django.contrib import admin
from .models import Author, Post, Tag
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_filter = ('author','tags')
    list_display = ('title', 'author')
    prepopulated_fields = { 'slug':('title',)}


admin.site.register(Post, BlogAdmin)
admin.site.register(Author)
admin.site.register(Tag)
