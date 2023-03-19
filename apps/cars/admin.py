from django.contrib import admin
from import_export.admin import ExportMixin
from apps.base.constants import date_filters
from apps.cars.models import Car
from apps.cars.admin_export_resources import CarResource
# Register your models here.

@admin.register(Car)
class CustomerAdmin(ExportMixin, admin.ModelAdmin):
    """Admin definition for the Car model"""
    resource_class = CarResource
    list_display = ('id', 'car_model_name', 'manufacturing_date',
                    'manufacturer_info', 'color',
                    'created_at', 'modified_at')
    list_per_page = 25
    list_filter = date_filters + ('car_model_name', 'manufacturer_info', 'color')
    readonly_fields = ('created_at', 'modified_at')
    ordering = ('-modified_at',)
    search_fields = ["id"]
