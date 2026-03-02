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
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='reset_password'),
    path('accounts/password_done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/<uidb64>/<token>', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password_complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),



]

# This might be needed, depending on your Django version
app_name = "ledger"
