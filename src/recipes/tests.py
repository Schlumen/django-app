from django.test import TestCase
from .models import Recipe

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name="Test Recipe", ingredients="Water, Ice",
                              cooking_time=5, description="Very awesome recipe description.")

    def test_return_string(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.__str__(), "Recipe: Test Recipe")

    def test_description(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.description,
                         "Very awesome recipe description.")

    def test_name_max_length(self):
        recipe = Recipe.objects.get(name="Test Recipe")
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(name="Test Recipe")
        max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(max_length, 512)

    def test_difficulty_max_length(self):
        recipe = Recipe.objects.get(name="Test Recipe")
        max_length = recipe._meta.get_field('difficulty').max_length
        self.assertEqual(max_length, 20)

    def test_difficulty_null_true(self):
        recipe = Recipe.objects.get(name="Test Recipe")
        allow_null = recipe._meta.get_field("difficulty").null
        self.assertTrue(allow_null)

    def test_creator_null_true(self):
        recipe = Recipe.objects.get(name="Test Recipe")
        allow_null = recipe._meta.get_field("creator").null
        self.assertTrue(allow_null)
