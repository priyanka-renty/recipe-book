from rest_framework import serializers

from .models import (
    Ingredient, Recipe, Step
)

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    

    class Meta:
        model = Recipe
        fields = ('id', 'recipe_name', 'owner', 'step',
                  'ingredients', 'is_public','created_at', 'updated_at')
