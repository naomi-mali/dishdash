from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm
from django.views.generic import ListView
from django.db.models import Q
from .forms import RecipeForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 9

def post_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment was submitted and is awaiting approval from admin'
    )

    comment_form = CommentForm()

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
    },
    )

class RecipeSearchList(ListView):
  
    model = Recipe
    template_name = 'blog/search_recipe.html'
    context_object_name = 'recipes'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(ingredients__icontains=query),
                status=1
            ).order_by('-created_on')
        else:
            queryset = Recipe.objects.none()
        return queryset

class AddRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "blog/add_recipe.html"
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = "Your recipe has been posted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super(AddRecipe, self).form_valid(form)

