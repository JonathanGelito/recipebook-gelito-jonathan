from django import forms

from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):

    class Meta:
        model=Recipe
        fields = '__all__'

        widgets = {
            'due_date': forms.TextInput(
                attrs={ 'type': 'datetime-local' }
            )
        }