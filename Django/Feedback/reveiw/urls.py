from django.urls import path
from reveiw import views

urlpatterns = [
    path('',views.ReviewView.as_view()),
    path('thank-you',views.ThankyouView.as_view()),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/favorite",views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>",views.SingleRView.as_view()),
]