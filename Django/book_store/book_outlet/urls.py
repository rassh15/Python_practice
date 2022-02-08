from django.contrib import admin
from django.urls import path
from book_outlet import views

urlpatterns = [
    path("", views.index),
    path('<slug:slug>', views.book_info, name='book_det')
]