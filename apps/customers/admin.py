from django.contrib import admin
from import_export.admin import ExportMixin
from apps.customers.models import Customer, Address
from apps.customers.admin_export_resources import CustomerResource
from apps.base.constants import date_filters


class AddressInline(admin.StackedInline):
    """Address staked inline with customer"""
    model = Address
    can_delete = False
    verbose_name_plural = 'Address'
    fk_name = 'customer'
    readonly_fields = ('created_at', 'modified_at')


@admin.register(Customer)
class CustomerAdmin(ExportMixin, admin.ModelAdmin):
    """Admin definition for the Customer model"""
    resource_class = CustomerResource
    inlines = (AddressInline,)
    list_display = ('id', 'first_name', 'last_name', 'age',
                    'date_of_birth', 'phone', 'email',
                    'created_at', 'modified_at')
    list_per_page = 25
    list_filter = date_filters
    readonly_fields = ('created_at', 'modified_at')
    ordering = ('-modified_at',)
    search_fields = ["id", "first_name", "last_name", "email", "phone"]
