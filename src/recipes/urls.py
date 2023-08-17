from django.urls import path
from .views import recipes_home
from .views import RecipeListView, RecipeDetailView
from .views import records, create_view

app_name = 'recipes'

urlpatterns = [
     path('', recipes_home),
     path('list/', RecipeListView.as_view(), name='list'),
     path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
     path('search/', records, name='search'),
     path('create/', create_view, name='create')
]
