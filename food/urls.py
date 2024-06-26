from django.urls import path
from .views import *
urlpatterns = [
    path("", HomeView.as_view(),name='home'),
    path("show-ing/", IngredientsListView.as_view(),name='show-ings'),
    path("show-ing/edit/", edit_ing,name='edit-ing'),
    path("show-recipes/",FoodRecipesListView.as_view(),name='show-recipe'),
    path("show-recipes/add/",FoodRecipesCreateView.as_view()),
    path("week/",weekly_plan,name='week'),
    path("suggested/",suggest,name='suggest'),


]
