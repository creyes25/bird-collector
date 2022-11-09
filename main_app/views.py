from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Care
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def birds_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', {'birds': birds})

def birds_details(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  feeding_form = FeedingForm()
  return render(request, 'birds/details.html', {'bird': bird, 'feeding_form': feeding_form})

class BirdCreate(CreateView):
  model = Bird
  fields = '__all__'
  success_url = '/birds/'

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['description', 'habitat', 'color', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'

# feeding
def add_feeding(request, bird_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save()
  return redirect('birds_details', bird_id=bird_id)

# care 
class CareCreate(CreateView):
  model = Care
  fields = '__all__'

class CareList(ListView):
  model = Care

class CareDetail(DetailView):
  model = Care