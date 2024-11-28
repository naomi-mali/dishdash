from django import forms
from django.core.exceptions import ValidationError
import bleach
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
        if not body or body.strip() == "":
            raise ValidationError('Comment body cannot be empty.')
        if len(body) > 500:
            raise ValidationError('Comments must be 500 characters or less.')
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
        if not title or title.strip() == "":
            raise ValidationError('Recipe title is required.')
        if len(title) > 100:
            raise ValidationError('Title cannot exceed 100 characters.')
        return title

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug or slug.strip() == "":
            raise ValidationError('Slug is required.')
        if not slug.isalnum():
            raise ValidationError('Slug must contain only alphanumeric characters.')
        return slug

    def clean_numeric_field(self, value, field_name):
        if value is None or value <= 0:
            raise ValidationError(f'{field_name} must be a positive number.')
        return value

    def clean_prep_time(self):
        return self.clean_numeric_field(self.cleaned_data.get('prep_time'), 'Preparation time')

    def clean_cooking_time(self):
        return self.clean_numeric_field(self.cleaned_data.get('cooking_time'), 'Cooking time')

    def clean_servings(self):
        return self.clean_numeric_field(self.cleaned_data.get('servings'), 'Servings')

    def clean_featured_image(self):
        """
        Validate the featured_image field to ensure the uploaded file is of a valid image type and size.
        """
        image = self.cleaned_data.get('featured_image')
        if image:
            if hasattr(image, 'content_type'):
                valid_content_types = ['image/jpeg', 'image/png', 'image/jpg']
                if image.content_type not in valid_content_types:
                    raise ValidationError("Only .jpg, .jpeg, and .png file types are supported.")
            if image.size > 2 * 1024 * 1024:  # 2 MB
                raise ValidationError("Image file size must not exceed 2MB.")
        return image

    def clean_ingredients(self):
        ingredients = self.cleaned_data.get('ingredients')
        if ingredients:
            ingredients = bleach.clean(ingredients, tags=['ul', 'ol', 'li', 'b', 'i', 'u', 'p', 'br'], strip=True)
        if not ingredients:
            raise ValidationError('Ingredients are required.')
        return ingredients

    def clean_instructions(self):
        instructions = self.cleaned_data.get('instructions')
        if instructions:
            instructions = bleach.clean(instructions, tags=['ul', 'ol', 'li', 'b', 'i', 'u', 'p', 'br'], strip=True)
        if not instructions:
            raise ValidationError('Instructions are required.')
        return instructions
