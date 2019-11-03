from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView
# Create your views here.


class HomeView(ListView):
    model = Item
    paginate_by=10
    template_name = 'home.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'
