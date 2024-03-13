from django.test import TestCase
from recipes.models import Category, Recipe, User
from unittest import skip

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name="Dessert"):
        return Category.objects.create(name=name)

    def make_author(
            self,
            first_name="John",
            last_name="Doe",
            username="johndoe",
            password="johndoe123",
            email="johndoe@email.com",
            ):
        return User.objects.create(
            first_name="John",
            last_name="Doe",
            username="johndoe",
            password="johndoe123",
            email="johndoe@email.com",
        )
    
    def make_recipe(
            self,
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
            category_data=None,
            author_data=None,
            ):
        if category_data is None:
            category_data = {}
        
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover,
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
        )
