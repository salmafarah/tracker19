# Create your models here.
from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django import forms

class Location (models.Model) : 
    name = models.CharField(max_length=100)
        #Shoppers, Metro... etc
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'pk': self.id})
    
    class Meta:
        ordering = ['-name']

class Partner(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-name']

class Entry (models.Model) : 
    date = models.DateField()
    time = models.TimeField()    
    comments = models.CharField(max_length=250)
    partner = models.ManyToManyField(Partner)
    location = models.ManyToManyField(Location)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.location











#     year = models.IntegerField()
#     month = models.IntegerField()
#     day = models.IntegerField()
#     hour = models.IntegerField()
#     min = models.IntegerField()
#     partner = models.CharField(max_length=100)