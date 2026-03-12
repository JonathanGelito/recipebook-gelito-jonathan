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

from django.urls import path

from .views import *

urlpatterns = [
    path("recipes/list", RecipeListView.as_view(), name='recipeslist'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add', RecipeAddView.as_view(), name="recipe_add"),
    path('recipe/<int:pk>/add_image', RecipeAddImageView.as_view(), name="recipe_add_image"),


]

# This might be needed, depending on your Django version
app_name = "ledger"
