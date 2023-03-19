from django.db import models
from apps.base.models import UUIDTimeStampedModel
from apps.cars.constants import CarModelChoices, ManufacturerChoices, ColorChoices
# Create your models here.

class Car(UUIDTimeStampedModel):
    """Car model to store car data"""
    car_model_name = models.CharField(max_length=50, choices=CarModelChoices.choices,
                                      default=CarModelChoices.DEMO_MODEL_DEFAULT)
    manufacturing_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    manufacturer_info = models.CharField(max_length=50, choices=ManufacturerChoices.choices,
                                         default=ManufacturerChoices.MN_MODEL_DEFAULT)
    color = models.CharField(max_length=50, choices=ColorChoices.choices, default=ColorChoices.COLOR_DEFAULT)

    def __str__(self) -> str:
        return f'{self.car_model_name} | {self.manufacturer_info} | {self.color}'
