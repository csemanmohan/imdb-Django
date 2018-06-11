from django.conf.urls import url,include
from django.contrib import admin
import rest_framework
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from dummyone.models import imdb
from rest_framework import generics

import django_filters
from django_filters.rest_framework import DjangoFilterBackend


# Serializers define the API representation.
class ImdbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = imdb
        fields = ('popularity', 'director', 'genre', 'imdb_score','name')

# ViewSets define the view behavior.
class ImdbViewSet(viewsets.ModelViewSet):
    queryset = imdb.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = ImdbSerializer
    filter_fields = ('popularity', 'director', 'genre', 'imdb_score','name')
    search_fields = ('popularity', 'director', 'genre', 'imdb_score','name')

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'imdb', ImdbViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^', include(router.urls)),
     url(r'^imdb/', include('dummyone.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
