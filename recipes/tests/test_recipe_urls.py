from django.test import TestCase
from django.urls import reverse


class RecipeURLSTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipe:list')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipe:category', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_recipe_url_is_correct(self):
        url = reverse('recipe:read', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')
