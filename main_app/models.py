from django.db import models
from django.urls import reverse

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

  # def get_absolute_url(self):
  #     return reverse("birds_detail", kwargs={"finch_id": self.id})