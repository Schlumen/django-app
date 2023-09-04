from django.db import models
from users.models import User

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=512)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20, null=True)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Recipe: {self.name}"
