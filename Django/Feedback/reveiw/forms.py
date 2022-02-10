from distutils.log import error
from socket import fromshare
from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name =  forms.CharField(label="Your Name", max_length=100,error_messages={
#         "required": "Your name must not be empty!",
#         "max_lenth": "Please enter a shorter name"
#     })

#     review_text = forms.CharField(label="Your Feedback",widget=forms.Textarea, max_length=200)
    
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' #or spefify [] to  select specific fields
        # exclude = 
        labels = {
            'user_name': "YOur name",
            'review_text': "Your Review",
            'rating': "Rating",
        }

        error_messages = {

            "user_name":{
                "required": "YOur name must not be empty",
                "max_length": "Enter in limit"
            }
        }

