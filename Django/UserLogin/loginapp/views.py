from django.shortcuts import redirect, render, HttpResponse, resolve_url
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib import messages
# Create your views here.
# plmnbv$4

def index(request):

    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def create_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        upass = request.POST.get('password')

        user = User.objects.create_user(uname,'abc@ysa', upass)
        user.save()
        messages.success(request, 'User Created')

    return render(request, 'createuser.html')


def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        upass = request.POST.get('password')

        # to authenthicate user        
        user = authenticate(username=uname, password=upass)
        if user is not None:
            login(request, user)
            return redirect('/')
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            messages.success(request, 'Invalid Credentials')
            return render(request, 'login.html')


    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login')

