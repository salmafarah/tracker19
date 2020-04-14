from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Entry

#Classes go here

class FormCreate(CreateView):
  model = Entry
  fields = [ 'year', 'month', 'day', 'hour', 'min', 'location', 'address', 'partner', 'comments' ]


# Create your views here.
def home(request): 
  return render(request, 'home.html')
  #static for now -> maybe show all other user as stretch goal
  pass
    







def about(request): #Static, read
  return render(request, 'about.html')








def signup (request):
  pass


















def profile(request): #shows all entries of the user, READ all 
  pass








def create_form(request): #Create
  pass








def one_entry(request): #shows one entry when clicked on #READ DELETE AND UPDATE goes here
  pass











# Home page -> Nav Bar: Home, About, Sign-in, Sign-up
# User page -> Nav Bar: Home, About, Sign-out, Profile
# Templates
# Home