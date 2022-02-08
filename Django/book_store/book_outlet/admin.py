from django.contrib import admin


# Register your models here.
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = { "slug": ("title",)}
    list_filter = ("rating", "title")
    list_display = ("title", "author")

admin.site.register(Book,BookAdmin)
admin.site.register(Author)


