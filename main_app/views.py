from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Bird

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
  return render(request, 'birds/details.html', {'bird': bird} )

class BirdCreate(CreateView):
  model = Bird
  fields = '__all__'
  success_url = '/birds/'
