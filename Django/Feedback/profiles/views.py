from msilib.schema import ListView
import profile
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from template.prof_form import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView


# Create your views here.

class CreateProfileView(CreateView):
    template_name = "prof_create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "prof_user_profiles.html"
    context_object_name = "profiles"

# def store_file(file):
#     with open("temp/image.jpg","wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()

#         return render(request, "prof_create_profile.html",{
#             "form":form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")

#         return render(request, "prof_create_profile.html",{
#             "form":submitted_form
#         })