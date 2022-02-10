import imp
import re
from django.shortcuts import render, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView

# Create your views here.

class ReviewView(FormView):

    form_class = ReviewForm
    template_name = "reveiw.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, 'reveiw.html',{'form':form})


    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/thank-you')


class ThankyouView(TemplateView):
    template_name = 'thank-you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "IT works"
        return context

class ReviewsListView(ListView):
    template_name = 'review_list.html'
    model = Review
    context_object_name = "reviews" #by default-> object_list

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__lt=3)
    #     return data



class SingleRView(DetailView):
    template_name = 'single_review.html'
    model = Review
    #access by smallcase model or object

