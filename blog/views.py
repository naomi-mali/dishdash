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
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required



# --- Recipe List View ---
class RecipeList(generic.ListView):
    """
    Displays a list of published recipes.
    Paginated to show 9 recipes per page.
    """
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = "blog/index.html"
    paginate_by = 9

# --- Recipe Detail View ---
def post_detail(request, slug):
    """
    Displays the details of a recipe.
    Allows comments to be submitted (pending approval).
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Your comment was submitted and is awaiting approval.')
        else:
            messages.error(request, 'There was an issue submitting your comment.')

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
        query = self.request.GET.get('q', '')
        if query:
            return Recipe.objects.filter(
                Q(title__icontains=query) | Q(ingredients__icontains=query),
                status=1
            ).order_by('-created_on')
        return Recipe.objects.none()

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
        form.instance.author = self.request.user
        form.instance.slug = self.generate_unique_slug(form.cleaned_data['title'])
        messages.success(self.request, "Your recipe has been posted successfully.")
        return super().form_valid(form)

    def generate_unique_slug(self, title):
        base_slug = slugify(title)
        slug = base_slug
        counter = 1
        while Recipe.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

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
        return reverse_lazy('home')

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        form.instance.author = self.request.user
        slug = form.cleaned_data['slug']
        if Recipe.objects.filter(slug=slug).exclude(pk=self.object.pk).exists():
            form.cleaned_data['slug'] = self.generate_unique_slug(slug)
        messages.success(self.request, "Your recipe has been updated successfully.")
        return super().form_valid(form)

    def generate_unique_slug(self, base_slug):
        slug = base_slug
        counter = 1
        while Recipe.objects.filter(slug=slug).exclude(pk=self.object.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

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

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your recipe has been deleted successfully.")
        return super().delete(request, *args, **kwargs)

# --- User's Draft Recipes View ---
class UserDrafts(LoginRequiredMixin, ListView):
    """
    Displays a list of draft recipes created by the logged-in user.
    Only shows drafts with status 'draft' (0).
    """
    template_name = "blog/my_drafts.html"
    model = Recipe
    context_object_name = "recipe_drafts"
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user, status=0).order_by('-created_on')

# --- Recipe Like/Unlike View ---
class RecipeLike(LoginRequiredMixin, View):
    """
    Allows logged-in users to like/unlike a recipe.
    Toggles the like status.
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
            messages.success(request, "You have unliked this recipe.")
        else:
            recipe.likes.add(request.user)
            messages.success(request, "You have liked this recipe.")

        return redirect(reverse('recipe_detail', args=[slug]))