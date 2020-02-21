from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    print(model)
    template_name = 'home.html'



