from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post
from django.db.models import Q
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    