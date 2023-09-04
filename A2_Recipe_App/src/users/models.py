from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=120)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return f"User: {self.username} ({self.name} - {self.email})"
