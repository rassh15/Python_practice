from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages




#  Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    # context = {
    #     "variable1": 'this is from views',
    #     "variable2": 'this is from second con'
    # }
    # return render(request, 'index.html',context)      
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("this is about page")
    return render(request, 'about.html')
    
def contact(request):
    # return HttpResponse("this is contact page")

    if request.method == 'POST':
        email = request.POST.get('email')
        epass = request.POST.get('pass')
        textarea = request.POST.get('textarea')

        contact = Contact(email=email,epass=epass,textarea=textarea)
        contact.save()
        messages.success(request, 'Your data is submitted')
    return render(request, 'contact.html')

def services(request):
    # return HttpResponse("this is service page")
    return render(request, 'services.html')