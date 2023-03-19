from import_export import resources
from apps.customers.models import Customer

class CustomerResource(resources.ModelResource):
    "Extended resource class for Customer model"
    class Meta:
        model = Customer
