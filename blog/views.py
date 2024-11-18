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


# Create your views here.

class RecipeList(generic.ListView):
    """
    Class-based view to display a list of published recipes.
    Displays 9 recipes per page, filtered to show only
    recipes with a status of 'published'.
    The recipes are ordered by the date they are created,
    with the latest ones appearing first.
    """
    queryset = Recipe.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 9


def post_detail(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
    except Recipe.DoesNotExist:
        raise Http404("Recipe not found")

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
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment was submitted and is awaiting approval from admin'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'There was an issue submitting your comment.'
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
    """
    View to display a list of recipes based on user search.
    Searches for recipes based on title, cuisine type, and description.
    Retrieves search results for only recipes with status 'published'.
    Displays 9 recipes per page.
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


class AddRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "blog/add_recipe.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Custom validation example
        if not form.cleaned_data['title']:
            raise ValidationError('Title is required.')

        form.instance.author = self.request.user
        success_message = "Your recipe has been posted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


class UpdateRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "blog/update_recipe.html"

    def get_success_url(self):
        # Redirect to the drafts page after a successful update
        return reverse_lazy('my_drafts')

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        # Custom validation example
        if not form.cleaned_data['title']:
            raise ValidationError('Title cannot be empty.')
        
        # Ensure the slug is unique after update
        slug = form.cleaned_data.get('slug')
        if slug:
            if Recipe.objects.filter(slug=slug).exclude(pk=self.object.pk).exists():
                form.cleaned_data['slug'] = f"{slug}-{self.object.pk}"

        form.instance.author = self.request.user
        success_message = "Your recipe has been updated successfully."
        messages.success(self.request, success_message)
        return super().form_valid(form)


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Class-based view to delete recipe.
    Checks if the user is authorized to delete the recipe.
    Manages delete request and override form_valid to
    display a success message to user after successful deletion.
    """
    model = Recipe
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, request, *args, **kwargs):
        success_message = "Your recipe has been deleted successfully."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().delete(request, *args, **kwargs)


class UserDrafts(ListView):
    """
    Class-based view to display user's draft recipes.
    Displays drafts created by the currently logged-in user.
    Only visible to the draft author.
    Returns a list of recipes with status of 'draft'.
    Displays 9 recipes per page.
    """
    template_name = "blog/my_drafts.html"
    model = Recipe
    context_object_name = "recipe_drafts"
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user, status=0)


class RecipeLike(View):
    """
    View to handle like/unlike recipe.
    Allows only logged-in users to like/unlike the recipe.
    Checks if the user has liked/unliked the recipe.
    Adds like if not/ removes like if yes.
    Redirects user back to the same page.
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if request.user.is_authenticated:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.likes.remove(request.user)
            else:
                recipe.likes.add(request.user)

        return redirect(reverse('recipe_detail', args=[slug]))
