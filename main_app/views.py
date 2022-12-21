from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Bird, Care
from .forms import FeedingForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
@csrf_exempt
def birds_index(request):
  birds = Bird.objects.filter(user=request.user)
  return render(request, 'birds/index.html', {'birds': birds})

@login_required
@csrf_exempt
def birds_details(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  cares_bird_doesnt_have = Care.objects.exclude(id__in = bird.cares.all().values_list('id'))

  feeding_form = FeedingForm()
  return render(request, 'birds/details.html', {'bird': bird, 'feeding_form': feeding_form, 'cares': cares_bird_doesnt_have})

class BirdCreate(LoginRequiredMixin, CreateView):
  model = Bird
  fields = ['name', 'type', 'description', 'habitat','color', 'age']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BirdUpdate(LoginRequiredMixin, UpdateView):
  model = Bird
  fields = ['description', 'habitat', 'color', 'age']

class BirdDelete(LoginRequiredMixin, DeleteView):
  model = Bird
  success_url = '/birds/'

# feeding
@login_required
@csrf_exempt
def add_feeding(request, bird_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save()
  return redirect('birds_details', bird_id=bird_id)

# care 
class CareCreate(LoginRequiredMixin, CreateView):
  model = Care
  fields = '__all__'

class CareList(LoginRequiredMixin, ListView):
  model = Care

class CareDetail(LoginRequiredMixin, DetailView):
  model = Care

class CareUpdate(LoginRequiredMixin, UpdateView):
  model = Care
  fields = ['name', 'benefits']

class CareDelete(LoginRequiredMixin, DeleteView):
  model = Care
  success_url = '/cares/'

@login_required
@csrf_exempt
def assoc_care(request, bird_id, care_id):
  Bird.objects.get(id=bird_id).cares.add(care_id)
  return redirect('birds_details', bird_id=bird_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('birds_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)