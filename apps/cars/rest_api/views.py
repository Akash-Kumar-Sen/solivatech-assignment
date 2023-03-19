from rest_framework.viewsets import ModelViewSet
from apps.cars.models import Car
from apps.cars.rest_api.serializers import CarSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt


class CarViewSet(ModelViewSet):
    """Viewset for car model"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)

    @classmethod
    def as_view(cls, actions=None, **kwargs):
        view = super(CarViewSet, cls).as_view(actions=actions, **kwargs)
        return csrf_exempt(view)