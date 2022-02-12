from email.headerregistry import Address
import imp
from django.contrib import admin
from .models import Author, Post, Tag, Comment
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_filter = ('author','tags')
    list_display = ('title', 'author')
    prepopulated_fields = { 'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name','post')

admin.site.register(Post, BlogAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
