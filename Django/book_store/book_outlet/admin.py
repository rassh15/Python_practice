from django.contrib import admin


# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = { "slug": ("title",)}
    list_filter = ("rating", "title")

admin.site.register(Book,BookAdmin)


