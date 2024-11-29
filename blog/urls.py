from . import views
from django.urls import path
from .views import (RecipeList, RecipeLike, RecipeSearchList, AddRecipe, UpdateRecipe, DeleteRecipe, UserDrafts)


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe_detail/<slug:slug>/', views.post_detail, name='recipe_detail'),
    path('recipe_search/', RecipeSearchList.as_view(), name='recipe_search'),
    path('add-recipe/', AddRecipe.as_view(), name='add_recipe'),
    path('recipe/update/<slug:slug>/', UpdateRecipe.as_view(), name='update_recipe'),
    path('recipe/delete/<slug:slug>/', DeleteRecipe.as_view(), name='delete_recipe'),
    path('recipe_drafts/', UserDrafts.as_view(), name='recipe_drafts'),
    path('recipe/<slug:slug>/like/', RecipeLike.as_view(), name='recipe_like'),
    path('my_drafts/', views.UserDrafts.as_view(), name='my_drafts'),
 
]

