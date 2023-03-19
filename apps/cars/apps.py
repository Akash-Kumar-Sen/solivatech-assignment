from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CarsConfig(AppConfig):
    name = "apps.cars"
    verbose_name = _("Cars")