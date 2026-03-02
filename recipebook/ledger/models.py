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
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient_detail", args=[str(self.name)])
    
    

    class Meta:
        ordering = ['name']
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    author = models.ForeignKey(Profile, 
                               on_delete=models.CASCADE, 
                               related_name="recipe")
    
    created_on = models.DateTimeField(null=False, 
                                      auto_now_add=True)
    
    updated_on = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):

    num_ingredients = models.CharField(max_length=50)

    name_ingredient = models.ForeignKey(Ingredient,
                                        on_delete=models.CASCADE,
                                        related_name="recipe")

    name_recipe = models.ForeignKey(Recipe,
                                    on_delete=models.CASCADE,
                                    related_name="ingredient")

    class Meta:
        ordering = ['name_ingredient']
        verbose_name = 'recipe_ingredient'
        verbose_name_plural = 'recipe_ingredients'

    def get_absolute_url(self):
        return reverse("recipeingredient_detail", args=[str(self.name)])

