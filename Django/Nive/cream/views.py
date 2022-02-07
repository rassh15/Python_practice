from curses.ascii import HT
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from httplib2 import Http
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "January": "This is the month of january",
    "February": "This is the month of february",
    "March": "This is the month of march",
    "April": "This is the month of april",
    "May": "This is the month of may",
    "June": "This is the month of june",
    "July": "This is the month of july",
    "August": None,
    "September": "This is the month of september",
    "October": "This is the month of october",
    "November": "This is the month of november",
    "December": None
    }
forward_month = list(monthly_challenges.keys())

def prod(request):
    # path_list = ""
    # for month in forward_month:
    #     redirect_path= reverse('month_chall', args=[month])
    #     path_list += f"<li><a href='{redirect_path}'>{month}</a></li>"
    
    return render(request, "index.html",{"months":forward_month})

# def january(request):
#     return HttpResponse("This is from january")

# def feb(request):
#     return HttpResponse("This is from february")

def month_chall_num(request, month):
    
    if month > len(forward_month):
        return HttpResponse("Invalid Month")
    
    redirect_path= reverse('month_chall', args=[forward_month[month-1]]) #vapor/january
    return HttpResponseRedirect(redirect_path)


    # return HttpResponseRedirect("/vapor/" + forward_month[month-1])

def month_chall(request, month):
    try:
        challenges_text = monthly_challenges[month]
        return render(request,"challenges.html",{"text":challenges_text, "month_title": month})
                
        # return HttpResponse(monthly_challenges[month])
    
    except:
        raise Http404()
