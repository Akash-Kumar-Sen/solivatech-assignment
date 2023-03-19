from rest_framework import serializers
from apps.customers.models import Customer, Address

class AddressBaseSerializer(serializers.ModelSerializer):
    """Base serializer for address model"""
    class Meta:
        model = Address
        fields = ['street_name', 'pincode', 'city', 
                  'state', 'country_code']


class CustomerSerializer(serializers.ModelSerializer):
    """Base serializer for customer model"""
    customer_address = AddressBaseSerializer('customer_address', read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'age',
                  'date_of_birth', 'phone', 'email', 'customer_address']