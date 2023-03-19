from django.urls import include, path
from rest_framework import routers

from apps.customers.rest_api.views import CustomerViewSet

router = routers.DefaultRouter()

router.register(r'customers', CustomerViewSet, basename='customers-v1')

app_name = 'customers'

urlpatterns = [
    path('', include(router.urls)),
]
