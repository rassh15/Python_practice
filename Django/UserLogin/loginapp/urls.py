from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from loginapp import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("login", views.login_view, name = 'login'),
    path("logout", views.logout_view, name = 'logout'),
    path('createuser', views.create_view, name = 'createuser')

]
