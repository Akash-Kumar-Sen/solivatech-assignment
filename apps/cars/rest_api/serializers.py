from rest_framework import serializers
from apps.cars.models import Car

class CarSerializer(serializers.ModelSerializer):
    """Base serializer for the Car Model"""
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'modified_at']
