
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(('authentication.urls','authentication'), namespace='authentication')),
    url(r'^api/', include(('recipe_api.urls','recipe_api') ,namespace='recipe_api')),
    url(r'^api-auth/', include('rest_framework.urls')),
]
