from django.db import models
from django import forms

# Create your models here.

class User(forms.ModelForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    phone_number = forms.IntegerField()

class TodoList(models.Model):
    title = models.CharField(max_length=100, blank=False)
    details = models.TextField(max_length=500)
    date = models.DateTimeField()
