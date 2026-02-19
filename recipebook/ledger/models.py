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

from django.db import models
from  datetime import datetime
from django.urls import reverse


# Create your models here.

class Ingredient(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):

    num_ingredients=models.DecimalField()
    name_ingredient=models.ForeignKey(Ingredient, 
                                on_delete=models.CASCADE, 
                                related_name="tasks")
    name_recipe=models.ForeignKey(Recipe, 
                                on_delete=models.CASCADE, 
                                related_name="tasks")
    def 