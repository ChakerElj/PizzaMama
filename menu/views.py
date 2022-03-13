from django.shortcuts import render
from django.views.generic import ListView
from .models import Pizza


# Create your views here.

class MenuPage(ListView):
    model = Pizza
    name = 'index'
    template_name = "index.html"
    context_object_name = 'pizzas'
    ordering = 'prix'
