from pyexpat import model
from turtle import update
from django.db import models


# Create your models here.
class Todolist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.name
lista = Todolist() 