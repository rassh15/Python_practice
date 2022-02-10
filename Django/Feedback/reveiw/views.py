import imp
import re
from django.shortcuts import render, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reveiw.html',{'form':form})


    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')


class ThankyouView(TemplateView):
    template_name = 'thank-you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "IT works"
        return context

class ReviewsListView(TemplateView):
    template_name = 'review_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context


class SingleRView(TemplateView):
    template_name = 'single_review.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviewid = kwargs["id"]
        selected_rev = Review.objects.get(pk=reviewid)
        context['reviews'] = selected_rev
        return context


