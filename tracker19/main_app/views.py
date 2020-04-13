from django.shortcuts import render
from django.http import HttpResponse


#Classes go here



# Create your views here.
def home(request): #static for now -> maybe show all other user as stretch goal
  pass
    # return render(request, 'home.html')







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