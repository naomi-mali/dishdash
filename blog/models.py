from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

def validate_nonzero(value):
    if value <= 0:
        raise ValidationError(f'{value} must be greater than zero.')

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_owner')
    prep_time = models.PositiveIntegerField(
        validators=[validate_nonzero, MaxValueValidator(300)], default=15)
    cooking_time = models.PositiveIntegerField(
        validators=[validate_nonzero, MaxValueValidator(600)], default=15)
    servings = models.PositiveIntegerField(
        validators=[validate_nonzero, MaxValueValidator(50)], default=1)
    # Macro nutrients in calories
    total_calories = models.PositiveIntegerField(
        validators=[validate_nonzero], default=0, help_text="Total calories in the recipe")
    calories_protein = models.PositiveIntegerField(
        validators=[validate_nonzero], default=0, help_text="Calories from protein")
    calories_carbs = models.PositiveIntegerField(
        validators=[validate_nonzero], default=0, help_text="Calories from carbohydrates")
    calories_fats = models.PositiveIntegerField(
        validators=[validate_nonzero], default=0, help_text="Calories from fats")
        
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    excerpt = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} | written by {self.author}'

class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Comment by {self.author} on {self.recipe}'



