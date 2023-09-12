from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeSearch
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd

# Create your views here.


def home(request):
    return render(request, "recipes/recipes_home.html")


@login_required
def search(request):
    form = RecipeSearch(request.POST or None)
    recipes = None
    recipes_df = None

    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        qs = Recipe.objects.filter(name__icontains=recipe_name)

        if qs:
            recipes = qs
            # Converting to Pandas Data Frame (not used in template, just for task)
            recipes_df = pd.DataFrame(qs.values())
            recipes_df = recipes_df.to_html()

    context = {
        "form": form,
        "recipes": recipes
    }

    return render(request, "recipes/search.html", context)


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/main.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail.html"
