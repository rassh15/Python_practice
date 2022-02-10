from django.urls import path
from reveiw import views

urlpatterns = [
    path('',views.review),
    path('thank-you',views.thankyou),
]