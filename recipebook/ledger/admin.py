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

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User 
from django.contrib import admin


# Register your models here.

from .models import Recipe, RecipeIngredient, Ingredient, Profile


class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient

    search_fields = ('name_ingredients', )

    fieldsets = [

        ('Details', {
            'fields': [
                ('num_ingredients'), 'name_ingredient', 'name_recipe'
            ]
        }),
    ]





class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientAdmin, ProfileInline]

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
