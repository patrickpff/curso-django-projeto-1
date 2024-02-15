from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from recipes.models import Category, Recipe, User


class RecipeViewTest(TestCase):

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

    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Dessert')
        author = User.objects.create(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            password="johndoe123",
            email="johndoe@email.com",
        )
        recipes = Recipe.objects.create(
            title='Pudim',
            description='Lorem ipsum dolor sit amet, consectetur '
            'adipiscing elit. Nulla ac nulla sit amet felis vestibulum'
            ' porta. Sed rhoncus nunc vel lobortis viverra.',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutes',
            servings=5,
            servings_unit='Portions',
            preparation_steps='Lorem ipsum dolor sit amet, consectetur '
            'adipiscing elit. Nulla ac nulla sit amet felis vestibulum'
            ' porta. Sed rhoncus nunc vel lobortis viverra. In hac '
            'habitasse platea dictumst. Vivamus aliquet, ligula ac '
            'faucibus sodales, ipsum orci auctor erat, vel aliquet est '
            'nisi sed orci. Maecenas mattis, nunc ac vulputate pharetra, '
            'tortor metus blandit neque, quis convallis massa sem at '
            'tortor. Proin pulvinar commodo aliquam. Quisque sit amet'
            ' euismod quam, quis interdum est. Integer dictum justo '
            'tristique ex varius, nec euismod quam egestas.'
            ' Sed eget consectetur ligula.',
            preparation_steps_is_html=False,
            is_published=True,
            cover=None,
            category=category,
            author=author,
        )
        response = self.client.get(reverse('recipe:list'))
        content = response.content.decode('UTF-8')
        response_context_recipes = response.context['recipes']
        
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

    # Detail
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipe:read', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_status_code_404_not_found(self):
        response = self.client.get(
            reverse('recipe:read', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)