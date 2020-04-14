from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Entry

#Classes go here

class FormCreate(CreateView):
  model = Entry
  fields = [ 'year', 'month', 'day', 'hour', 'min', 'location', 'address', 'partner', 'comments' ]

class EntryUpdate(UpdateView):
  model = Entry
  fields = [ 'year', 'month', 'day', 'hour', 'min', 'location', 'address', 'partner', 'comments' ]

class EntryDelete(DeleteView):
  model = Entry
  success_url = '/entry/'




# Create your views here.
def home(request): #static for now -> maybe show all other user as stretch goal
  pass
    # return render(request, 'home.html')







def about(request): #Static, read
  return render(request, 'about.html')

























def create_form(request): #Create
  pass



















def entry_detail(request, entry_id):
  entry = Entry.objects.get(id=entry_id)
  # instantiate FeedingForm to be rendered in the template
  return render(request, 'entry/detail.html', {
    # pass the cat and feeding_form as context
    'entry': entry
  })

def entry_index(request):
  entry = Entry.objects.all()
  return render(request, 'entry/index.html', { 'entry': entry })



# Home page -> Nav Bar: Home, About, Sign-in, Sign-up
# User page -> Nav Bar: Home, About, Sign-out, Profile
# Templates
# Home



