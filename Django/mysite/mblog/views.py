from django.shortcuts import render , get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request, "index.html", {"posts": latest_post})

def posts(request):
    postdb = Post.objects.all().order_by("-date")
    return render(request, "all-post.html",{"all_post": postdb})

def post_detail(request,slug):
    
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "post-details.html",{'identified_post': identified_post,
    'post_tags': identified_post.tags.all()})