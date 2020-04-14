from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Entry


#Classes go here

class FormCreate(LoginRequiredMixin,CreateView):
  model = Entry
  fields = [ 'year', 'month', 'day', 'hour', 'min', 'location', 'address', 'partner', 'comments' ]
  success_url = '/entry/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class EntryUpdate(LoginRequiredMixin,UpdateView):
  model = Entry
  fields = [ 'year', 'month', 'day', 'hour', 'min', 'location', 'address', 'partner', 'comments' ]

class EntryDelete(LoginRequiredMixin,DeleteView):
  model = Entry
  success_url = '/entry/'
  
  
  
  
  




# Create your views here.
def home(request): #static for now -> maybe show all other user as stretch goal
    return render(request, 'home/home.html')
  
  
  







def about(request): #Static, read
  return render(request, 'about/about.html')









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
















@login_required 
def entry_detail(request, entry_id):
  entry = Entry.objects.get(id=entry_id)
  return render(request, 'entry/detail.html', {
    'entry': entry
  })








@login_required 
def entry_index(request):
  entry = Entry.objects.all()
  return render(request, 'entry/index.html', { 'entry': entry })





# Home page -> Nav Bar: Home, About, Sign-in, Sign-up
# User page -> Nav Bar: Home, About, Sign-out, Profile
# Templates
# Home



