from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import render




#Classes go here



# Create your views here.
def home(request): #static for now -> maybe show all other user as stretch goal
    return render(request, 'base.html')







def about(request): #Static, read
  return render(request, 'about.html')








def signup(request):
  error_message = ''
  if request.method == 'POST': 
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
      user = form.save()
      login(request,user)
      return redirect('index')
    else: 
      error_message = 'Invalid sign up - try again SiS'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

















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