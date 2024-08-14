from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm
from django.views.generic import ListView
from django.db.models import Q
from .forms import RecipeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse




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

class UpdateRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "blog/update_recipe.html"
    
    def get_success_url(self):
        # Redirect to the detail page of the updated recipe
        return reverse_lazy('recipe_detail', kwargs={'slug': self.object.slug})
    
    def test_func(self):
        # Ensures that only the author of the recipe can edit it
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        # Associates the current user as the author
        form.instance.author = self.request.user
        success_message = "Your recipe has been updated successfully."
        messages.success(self.request, success_message)
        return super().form_valid(form)

class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user == self.get_object().author

    def delete(self, request, *args, **kwargs):
        # Perform the deletion and get the response
        response = super().delete(request, *args, **kwargs)
        # Add a success message
        messages.success(self.request, "Your recipe has been deleted successfully.")
        return response

class UserDrafts(ListView):

    template_name = "blog/my_drafts.html"
    model = Recipe
    context_object_name = "recipe_drafts"
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user, status=0)

class RecipeLike(View):
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if request.user.is_authenticated:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.likes.remove(request.user)
            else:
                recipe.likes.add(request.user)

        return redirect(reverse('recipe_detail', args=[slug]))

 