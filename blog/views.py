from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm, RecipeForm
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError


# --- Recipe List View ---
class RecipeList(generic.ListView):
    """
    Displays a list of published recipes.
    Paginated to show 9 recipes per page.
    """
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 9


# --- Recipe Detail View ---
def post_detail(request, slug):
    """
    Displays the details of a recipe.
    Allows comments to be submitted (pending approval).
    """
    try:
        recipe = Recipe.objects.get(slug=slug)
    except Recipe.DoesNotExist:
        raise Http404("Recipe not found")

    # Ensure the recipe is visible if it's published or the user is the author/admin
    if recipe.status == 0 and (not request.user.is_staff and request.user != recipe.author):
        raise Http404("Recipe is in draft status and cannot be viewed by this user.")

    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your comment was submitted and is awaiting approval from admin')
        else:
            messages.add_message(request, messages.ERROR,
                                 'There was an issue submitting your comment.')

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


# --- Recipe Search View ---
class RecipeSearchList(ListView):
    """
    Displays a list of recipes based on the search query.
    Filters by title and ingredients.
    Only shows published recipes.
    """
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


# --- Add Recipe View ---
class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Allows logged-in users to add a new recipe.
    Validates the form and saves the recipe with the current user as the author.
    """
    model = Recipe
    form_class = RecipeForm
    template_name = "blog/add_recipe.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Ensure the title is not empty
        if not form.cleaned_data['title']:
            raise ValidationError('Title is required.')

        form.instance.author = self.request.user
        success_message = "Your recipe has been posted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


# --- Update Recipe View ---
class UpdateRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows users to update their recipes.
    Ensures only the author can update their recipe.
    Validates and ensures the slug is unique after update.
    """
    model = Recipe
    form_class = RecipeForm
    template_name = "blog/update_recipe.html"

    def get_success_url(self):
        # Redirect to the home page after successful update
        return reverse_lazy('home')

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        # Ensure the title is not empty
        if not form.cleaned_data['title']:
            raise ValidationError('Title cannot be empty.')
        
        # Ensure the slug is unique
        slug = form.cleaned_data.get('slug')
        if slug:
            if Recipe.objects.filter(slug=slug).exclude(pk=self.object.pk).exists():
                form.cleaned_data['slug'] = f"{slug}-{self.object.pk}"

        form.instance.author = self.request.user
        success_message = "Your recipe has been updated successfully."
        messages.success(self.request, success_message)
        return super().form_valid(form)


# --- Delete Recipe View ---
class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows users to delete their recipes.
    Ensures only the author can delete the recipe.
    Displays a success message upon deletion.
    """
    model = Recipe
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, request, *args, **kwargs):
        success_message = "Your recipe has been deleted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().delete(request, *args, **kwargs)


# --- User's Draft Recipes View ---
class UserDrafts(ListView):
    """
    Displays a list of draft recipes created by the logged-in user.
    Only shows drafts with status 'draft' (0).
    """
    template_name = "blog/my_drafts.html"
    model = Recipe
    context_object_name = "recipe_drafts"
    paginate_by = 6

    def get_queryset(self):
        # Filter for drafts (status=0) and order by creation date
        return Recipe.objects.filter(author=self.request.user, status=0).order_by('-created_on')


# --- Recipe Like/Unlike View ---
class RecipeLike(View):
    """
    Allows logged-in users to like/unlike a recipe.
    Toggles the like status.
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if request.user.is_authenticated:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.likes.remove(request.user)
            else:
                recipe.likes.add(request.user)

        return redirect(reverse('recipe_detail', args=[slug]))
