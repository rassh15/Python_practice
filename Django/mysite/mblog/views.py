from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def posts(request):
    return render(request, "all-post.html")

def post_detail(request,slug):
    return render(request, "post-details.html")