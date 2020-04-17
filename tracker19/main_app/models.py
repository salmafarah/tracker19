from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django import forms 
from datetime import datetime
from django.utils.safestring import mark_safe

HealthStatus= (
    ('choice1', 'I’ve been dignoised with COVID-19 and would like to create a record of my whereabouts'), 
    ('choice2','I’ve recovered from COVID-19, but would like to track my whereabouts'), 
    ('choice3','I’ve not been tested for COVID-19, but feel sick and want to track my whereabouts'), 
    ('choice4','I do not have COVID-19 but would like to track my whereabout') 
)

Feeling = (
    ('choice1', mark_safe('&#128524;')),
    ('choice1', mark_safe('&#128577;')),
    ('choice1', mark_safe('&#128555;')),
    ('choice1', mark_safe('&#128567;')),
)

class Location (models.Model) : 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'pk': self.id})
        
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

class Health(models.Model):
    date = models.DateField()
    health = models.CharField('Which option best describes your health status',choices= HealthStatus, max_length=100)
    feeling = models.CharField('How do you feel today ?',  choices= Feeling, max_length=100)
    symptoms = models.CharField('What are your current symptoms ?', max_length=250)
    comments = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_feeling_display()}"
    
    def get_absolute_url(self):
        return reverse('health_detail', kwargs={'health_id': self.id})

