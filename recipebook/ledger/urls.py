from django.urls import path

from .views import *

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe_list'),
    path('recipe/1', recipe_1, name="recipe_1"),
    path('recipe/2', recipe_2, name="recipe_2")



]

# This might be needed, depending on your Django version
app_name = "ledger"