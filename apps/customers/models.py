from django.db import models
from apps.base.models import UUIDTimeStampedModel
# Create your models here.


class Customer(UUIDTimeStampedModel):
    """Model to store customer info
    """
    first_name  = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateTimeField(auto_now=False, auto_now_add=False)
    phone = models.CharField(max_length=10, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class Address(UUIDTimeStampedModel):
    """Model to store customer address
    """
    street_name = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country_code = models.CharField(max_length=3)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='customer_address',
                                    blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.customer} address'