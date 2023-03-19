from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from apps.customers.models import Customer, Address
from apps.customers.rest_api.serializers import CustomerSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


class CustomerViewSet(ModelViewSet):
    """Viewset for car model"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)

    @classmethod
    def as_view(cls, actions=None, **kwargs):
        view = super(CustomerViewSet, cls).as_view(actions=actions, **kwargs)
        return csrf_exempt(view)

    @action(detail=True, methods=['post'])
    def create_customer_address(self, request, *args, **kwargs):
        """View to create customer address"""
        street_name = request.data.get("street_name")
        pincode = request.data.get("pincode")
        state = request.data.get("state")
        city = request.data.get("city")
        country_code = request.data.get("country_code")

        customer_object = self.get_object()

        address = Address.objects.create(
            street_name=street_name,
            pincode=pincode,
            state=state,
            city=city,
            country_code=country_code,
            customer=customer_object
        )

        serialized_data = CustomerSerializer(customer_object).data
        return Response(serialized_data, status=status.HTTP_201_CREATED)
