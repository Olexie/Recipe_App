from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

# Create your views here.
def recipes_home(request):
    return render(request, 'recipes/recipes_home.html')