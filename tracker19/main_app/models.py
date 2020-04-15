#To Do - change datefield 





# Create your models here.
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django import forms
from datetime import datetime


class Entry (models.Model) : 
    date = models.DateField()    
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    partner = models.CharField(max_length=100)
    comments = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location


#     year = models.IntegerField()
#     month = models.IntegerField()
#     day = models.IntegerField()
#     hour = models.IntegerField()
#     min = models.IntegerField()