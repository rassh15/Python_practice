from django.shortcuts import render, HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.

def review(request):

    if request.method=="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank-you')

    else:
        form = ReviewForm()
    return render(request, 'reveiw.html',{'form':form})

def thankyou(request):
    return render(request, 'thank-you.html')    
