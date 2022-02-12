from ast import Return
import imp
from re import template
from urllib import request
import django
from django.shortcuts import render , get_object_or_404
from matplotlib.style import context
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.views import View
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

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

    
class PostDetailView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved_for_later = post_id in stored_posts
        else:
          is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
    
        context = {
            "post":post,
            "post_tags":post.tags.all(),
            "comment_form":CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "post-details.html",context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail",args=[slug]))
        else:
            print("Error: ",comment_form.errors)
        
        context = {
            "post":post,
            "post_tags":post.tags.all(),
            "comment_form":comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)

        }
        return render(request, "post-details.html",context)

    
class ReadLaterView(View):
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or  len(stored_posts)==0:
            context['posts']=[]
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context['has_posts'] = True

        return render(request, 'stored-posts.html',context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST['post_id'])
        if post_id not in stored_posts:
              stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")
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