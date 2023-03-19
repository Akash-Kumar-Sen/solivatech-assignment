from import_export import resources
from apps.cars.models import Car

class CarResource(resources.ModelResource):
    "Extended resource class for Car model"
    class Meta:
        model = Car
