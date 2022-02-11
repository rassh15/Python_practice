from re import template
from django.shortcuts import render , get_object_or_404
from matplotlib.style import context
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class StartingPageView(ListView):
    template_name = "index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data
    

class AllPostView(ListView):
    template_name = "all-post.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_post"

    
class PostDetailView(DetailView):
    template_name = "post-details.html"
    model = Post
    context_object_name = "identified_post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
    

'''

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

    '''