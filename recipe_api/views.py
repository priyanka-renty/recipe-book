from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import (ValidationError, PermissionDenied)
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import (Recipe,Ingredient,Step)
from .serializers import (RecipeSerializer)

class RecipesViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    permission_classes = (IsAuthenticated,)
    queryset = Recipe.objects.all()
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('owner',)
    filter_fields = ('owner',)

    def get_queryset(self):
        queryset = Recipe.objects.all()
        return queryset

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create recipes")
        return super().create(request, *args, **kwargs)

    # user can only delete recipe he created
    def destroy(self, request, *args, **kwargs):
        recipe  = Recipe.objects.get(pk=self.kwargs["pk"])
        if not request.user == recipe.owner:
            raise PermissionDenied(
                "You have no permissions to delete this recipe")
        return super().destroy(request, *args, **kwargs)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicRecipes(generics.ListAPIView):

    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Recipe.objects.all().filter(is_public=True)
        return queryset
    serializer_class = RecipeSerializer


class PublicRecipesDetail(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Recipe.objects.all().filter(is_public=True)
        return queryset
    serializer_class = RecipeSerializer
