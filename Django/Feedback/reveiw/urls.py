from django.urls import path
from reveiw import views

urlpatterns = [
    path('',views.ReviewView.as_view()),
    path('thank-you',views.ThankyouView.as_view()),
]