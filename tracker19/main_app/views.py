from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import HttpResponse
from .models import Entry, Health
from .forms import EntryForm, HealthForm 


#Classes go here

class FormCreate(LoginRequiredMixin,CreateView):
  model = Entry
  form_class = EntryForm
  # fields = [ 'date', 'location', 'address', 'partner', 'comments' ]
  success_url = '/entry/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class EntryUpdate(LoginRequiredMixin,UpdateView):
  model = Entry
  fields = ['location', 'address', 'partner', 'comments' ]
  success_url = '/entry/'

class EntryDelete(LoginRequiredMixin,DeleteView):
  model = Entry
  success_url = '/entry/'



class HealthCreate(LoginRequiredMixin,CreateView):
  model = Health
  form_class = HealthForm 
  success_url = '/health/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class HealthUpdate(LoginRequiredMixin,UpdateView):
  model = Entry
  fields = ['location', 'address', 'partner', 'comments' ]
  success_url = '/health/'


def health_index(request):
  health = Health.objects.filter(user=request.user)
  return render(request, 'health/index.html', { 'health': health })
  
def anonymous(request): 
    return render(request, 'anonymous/anonymous.html')








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
      return redirect('health_create')
    else: 
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)






# @login_required 
# def date_entry(request):
#   context = {}
#   context['form'] = DateForm()
#   return render(request, 'main_app/date_entry.html', context)







@login_required 
def entry_detail(request, entry_id):
  entry = Entry.objects.get(id=entry_id)
  return render(request, 'entry/detail.html', {
    'entry': entry
  })








@login_required 
def entry_index(request):
  entry = Entry.objects.filter(user=request.user)
  return render(request, 'entry/index.html', { 'entry': entry })





# Home page -> Nav Bar: Home, About, Sign-in, Sign-up
# User page -> Nav Bar: Home, About, Sign-out, Profile
# Templates
# Home



