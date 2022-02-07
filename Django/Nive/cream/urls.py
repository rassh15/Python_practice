
from django.contrib import admin
from django.urls import path
from cream import views

urlpatterns = [
    path('',views.prod,name='prod'),
    path('<int:month>',views.month_chall_num,name='month_chall_num'),
    path('<str:month>',views.month_chall,name='month_chall'),
    
]
