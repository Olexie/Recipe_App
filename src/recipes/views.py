from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

# Create your views here.
def recipes_home(request):
    return render(request, 'recipes/recipes_home.html')