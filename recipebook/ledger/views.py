# Jonathan II A. Gelito
# 242043
# Febrauary 9, 2025

# I have not discussed the Python language code in my program
# with anyone other than my instructor or the teaching assistants
# assigned to this course.

# I have not used Python language code obtained from another student,
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program
# was obtained from another source, such as a textbook or website,
# that has been clearly noted with a proper citation in the comments
# of my program.

from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import Taskforms
from .models import Recipe, RecipeIngredient, Ingredient

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



ingredients = Ingredient.objects.all()

def recipe_detail(request, id):

    recipe = Recipe.objects.get(pk=id)

    return render(request, 'ledger/recipe_detail.html', {
        "recipe": recipe,
    })


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipes_list.html"

class RecipeDetailView(LoginRequiredMixin,DetailView):
    model = Recipe
    template_name = "ledger/recipes_detail.html"
    redirect_field_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        context["ingredients"] = RecipeIngredient.objects.filter(
            name_recipe=recipe
        )
        return context

