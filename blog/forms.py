from django import forms
from django.core.exceptions import ValidationError
from .models import Comment, Recipe

class CommentForm(forms.ModelForm):
    """
    Comment Form to add comments
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Leave your comment here',
        }

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if not body:
            raise ValidationError('Comment body cannot be empty.')
        return body


class RecipeForm(forms.ModelForm):
    """
    Recipe Form to create/add new recipes
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'slug', 
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
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the recipe title...'}),
            'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'prep_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter preparation time in minutes'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter cooking time in minutes'}),
            'servings': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of servings'}),
            'total_calories': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter total calories'}),
            'calories_protein': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter calories from protein'}),
            'calories_carbs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter calories from carbohydrates'}),
            'calories_fats': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter calories from fats'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'List ingredients here...'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Provide cooking instructions here...'}),
            'status': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Recipe title is required.')
        return title

    def clean_ingredients(self):
        ingredients = self.cleaned_data.get('ingredients')
        if not ingredients:
            raise ValidationError('Ingredients are required.')
        return ingredients

    def clean_instructions(self):
        instructions = self.cleaned_data.get('instructions')
        if not instructions:
            raise ValidationError('Instructions are required.')
        return instructions

    def clean_featured_image(self):
        """
        Validate the featured_image field to ensure the uploaded file is of a valid image type.
        """
        image = self.cleaned_data.get('featured_image')
        if image:
            # Validate uploaded image MIME type
            if hasattr(image, 'content_type'):
                valid_content_types = ['image/jpeg', 'image/png', 'image/jpg']
                if image.content_type not in valid_content_types:
                    raise ValidationError("Only .jpg, .jpeg, and .png file types are supported.")
        return image
