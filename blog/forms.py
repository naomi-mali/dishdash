from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class Bootstrap4TextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})['class'] = 'form-control'
        super().__init__(*args, **kwargs)


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'title', 
            'featured_image', 
            'prep_time', 
            'cooking_time', 
            'servings', 
            'total_calories', 
            'calories_protein', 
            'calories_carbs', 
            'calories_fats', 
            'ingredients', 
            'instructions',
            'status',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'prep_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'servings': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_calories': forms.NumberInput(attrs={'class': 'form-control'}),
            'calories_protein': forms.NumberInput(attrs={'class': 'form-control'}),
            'calories_carbs': forms.NumberInput(attrs={'class': 'form-control'}),
            'calories_fats': forms.NumberInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect()
        }