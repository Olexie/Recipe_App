from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time= models.FloatField(help_text=' minutes')
    ingredients =models.CharField(max_length=300, help_text=' please separate ingredients with commas')
    description = models.TextField(default='add your notes here')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) <4:
            difficulty = 'Easy'
        elif self.cooking_time <10 and len(ingredients) >=4:
            difficulty = 'Medium'
        elif self.cooking_time >=10 and len(ingredients) <4:
            difficulty = 'Intermediate'
        elif self.cooking_time >=10 and len(ingredients) >=4:
            difficulty = 'Hard'
        return difficulty
    
    def __str__(self):
        return self.name
    
    