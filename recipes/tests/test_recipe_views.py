from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeViewTest(RecipeTestBase):
    # Home
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipe:list'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipe:list'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_correct_template(self):
        response = self.client.get(reverse('recipe:list'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipe:list'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('UTF-8')
        )

    def test_recipe_home_shows_no_recipes_found_if_no_recipes_fail(self):
        response = self.client.get(reverse('recipe:list'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('UTF-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipe:list'))
        content = response.content.decode('UTF-8')
        response_context_recipes = response.context['recipes']
        # Check if the created recipe is in the page
        self.assertIn('Pudim', content)
        self.assertIn('10 Minutes', content)
        self.assertIn('5 Portions', content)
        self.assertEqual(len(response_context_recipes), 1)

    # Category
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipe:category', kwargs={'id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_code_404_not_found(self):
        response = self.client.get(
            reverse('recipe:category', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        name = "Breakfast"
        self.make_recipe(category_data={'name': name})
        response = self.client.get(
            reverse('recipe:category', kwargs={'id': 1})
            )
        content = response.content.decode('UTF-8')
        self.assertIn(name, content)
        
    #    recipe = self.make_recipe(title=title)
    #    response = self.client.get(
    #        reverse('recipe:category', kwargs={id: recipe.id})
    #        )
    #    content = response.content.decode('UTF-8')
    #    # Check if the created recipe is in the page
    #    self.assertIn(title, content)

    # Detail
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipe:read', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_status_code_404_not_found(self):
        response = self.client.get(
            reverse('recipe:read', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
