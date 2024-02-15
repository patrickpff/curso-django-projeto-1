from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views


class RecipeViewTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipe:list'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipe:category', kwargs={'id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipe:read', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)