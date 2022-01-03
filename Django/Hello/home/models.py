from django.db import models

# Create your models here.

#dealing with database

class Contact(models.Model):
    
    email = models.CharField(max_length=122)
    epass = models.CharField(max_length=20)
    textarea = models.TextField()

