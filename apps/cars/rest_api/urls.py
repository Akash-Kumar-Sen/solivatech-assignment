from django.urls import include, path
from rest_framework import routers

from apps.cars.rest_api.views import CarViewSet

router = routers.DefaultRouter()

router.register(r'cars', CarViewSet, basename='cars-v1')

app_name = 'cars'

urlpatterns = [
    path('', include(router.urls)),
]
