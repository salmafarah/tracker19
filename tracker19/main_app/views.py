from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import HttpResponse
from .models import Entry, Partner, Location
from .forms import EntryForm


#Classes go here

class FormCreate(LoginRequiredMixin,CreateView):
  model = Entry
  form_class = EntryForm
  success_url = '/entry/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class EntryUpdate(LoginRequiredMixin,UpdateView):
  model = Entry
  fields = ['comments' ]
  success_url = '/entry/'

class EntryDelete(LoginRequiredMixin,DeleteView):
  model = Entry
  success_url = '/entry/'
class LocationList(ListView):
  model = Location

class LocationDetail(DetailView):
  model = Location

class LocationCreate(CreateView):
  model = Location
  fields = '__all__'

class LocationUpdate(UpdateView):
  model = Location
  fields = ['name', 'address', 'latitude', 'longitude']

class LocationDelete(DeleteView):
  model = Location
  success_url = '/location/'

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
      return redirect('entry_index')
    else: 
      error_message = 'Invalid sign up - try again SiS'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


@login_required 
def entry_index(request):
  entry = Entry.objects.filter(user=request.user)
  return render(request, 'entry/index.html', { 'entry': entry })



@login_required 
def entry_detail(request, entry_id):
  entry = Entry.objects.get(id=entry_id)
  no_partners = Partner.objects.exclude(id__in = entry.partner.all().values_list('id'))
  no_location = Location.objects.exclude(id__in = entry.location.all().values_list('id'))
  return render(request, 'entry/detail.html', {
    'entry': entry,
    'partner': no_partners,
    'locations': no_location
  })


@login_required
def assoc_partner(request, entry_id, partner_id):
  Entry.objects.get(id=entry_id).partner.add(partner_id)
  return redirect('detail', entry_id=entry_id)

@login_required
def unassoc_partner(request, entry_id, partner_id):
  Entry.objects.get(id=entry_id).partner.remove(partner_id)
  return redirect('detail', entry_id=entry_id)

def picked_location(request, entry_id, location_id):
  Entry.objects.get(id=entry_id).location.add(location_id)
  return redirect('detail', entry_id=entry_id)


def unpicked_location(request, entry_id, location_id):
  Entry.objects.get(id=entry_id).location.remove(location_id)
  return redirect('detail', entry_id=entry_id)







# Home page -> Nav Bar: Home, About, Sign-in, Sign-up
# User page -> Nav Bar: Home, About, Sign-out, Profile
# Templates
# Home








'''
@login_required
def add_partner(request, entry_id):
    form = PartnerForm(request.POST)
    if form.is_valid():
        new_partner = form.save(commit=False)
        new_partner.entry_id = entry_id
        new_partner.save()
    return redirect('detail', entry_id = entry_id)
'''






