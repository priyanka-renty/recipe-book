from django.db import models
from authentication.models import User

class Step(models.Model):
    step = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.step

class Ingredient(models.Model):
    ingredients = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.ingredients

class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.recipe_name
