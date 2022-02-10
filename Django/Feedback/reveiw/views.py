from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def review(request):

    if request.method=="POST":
        entered_username = request.POST['username']
        if entered_username=="":
            return render(request, 'reveiw.html',{"has_error":True})
        return HttpResponseRedirect('/thank-you')
    return render(request, 'reveiw.html',{"has_error":False})

def thankyou(request):
    return render(request, 'thank-you.html')    
