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

from .models import Recipe, RecipeIngredient, Ingredient

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    return HttpResponse('Hello World! This came from the index view')







class RecipeView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html' 

class RecipeIngredientView(DetailView):
    model = RecipeIngredient
    template_name = 'ledger/recipes_detail.html' 


