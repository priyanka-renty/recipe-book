from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import (RecipesViewSet,PublicRecipes)

router = DefaultRouter()

router.register('recipes', RecipesViewSet, base_name='recipes')

custom_urlpatterns = [url(r'public-recipes/$', PublicRecipes.as_view(), name='public_recipes'),]

urlpatterns = router.urls

urlpatterns += custom_urlpatterns
