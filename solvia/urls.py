from django.contrib import admin
from django.urls import path, re_path, include

from solvia.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    re_path(r"^api/v1/", include("apps.cars.rest_api.urls", namespace="cars_v1")),
    re_path(r"^api/v1/", include("apps.customers.rest_api.urls", namespace="customers_v1")),
]
