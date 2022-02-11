from django.urls import path
from . import views

urlpatterns = [
    path('',views.StartingPageView.as_view(), name="starting"),
    path('posts',views.AllPostView.as_view(), name = 'post'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name= 'post-detail')#posts/my-first-post
]
