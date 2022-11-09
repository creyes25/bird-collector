from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

FOODS = (
  ('SE', 'Seeds'),
  ('GR', 'Grains'),
  ('NU', 'Nuts'),
  ('FR', 'Fruits'),
  ('BE', 'Berries'),
  ('VE', 'Veggies'),
)

# Create your models here.
class Bird(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  habitat = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("birds_details", kwargs={"bird_id": self.id})

class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  food = models.CharField(
    max_length=2,
    choices=FOODS,
    default = FOODS[0][0]
  )
  bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_food_display()} for {self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']
