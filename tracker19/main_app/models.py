#To Do - change datefield 





# Create your models here.
from django.db import models

class Entry (models.Model) : 
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    min = models.IntegerField()
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    partner = models.CharField(max_length=100)
    comments = models.CharField(max_length=250)

    def __str__(self):
        return self.location

    




