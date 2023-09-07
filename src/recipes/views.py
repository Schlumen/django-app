from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, "recipes/recipes_home.html")


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/main.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail.html"
