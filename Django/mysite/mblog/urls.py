from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="starting"),
    path('posts',views.posts, name = 'post'),
    path('post/<slug:slug>', views.post_detail, name= 'post-detail')#posts/my-first-post
]
