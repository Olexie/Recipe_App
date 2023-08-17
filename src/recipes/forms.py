from django import forms

CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

DIFFICULTY__CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard'),
)

class DifficultySearchForm(forms.Form):
    ecipe_diff = forms.ChoiceField(choices=DIFFICULTY__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class CreateRecipeForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    cooking_time = forms.IntegerField(help_text='in minutes', required=False)
    ingredients = forms.CharField(max_length=300, required=False)
    description = forms.CharField(max_length=300, required=False)