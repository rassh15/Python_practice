from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def review(request):

    if request.method=="POST":
        entered_username = request.POST['username']
        return HttpResponseRedirect('/thank-you')
    return render(request, 'reveiw.html')

def thankyou(request):
    return render(request, 'thank-you.html')    
