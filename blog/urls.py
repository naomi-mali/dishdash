from . import views
from django.urls import path
from .views import RecipeSearchList

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe_detail/<slug:slug>/', views.post_detail, name='recipe_detail'),
    path('recipe_search/', RecipeSearchList.as_view(), name='recipe_search'),
]