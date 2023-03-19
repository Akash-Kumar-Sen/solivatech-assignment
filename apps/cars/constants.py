from django.db import models

class CarModelChoices(models.TextChoices):
    DEMO_MODEL_1 = "Demo Model 1"
    DEMO_MODEL_2 = "Demo Model 2"
    DEMO_MODEL_3 = "Demo Model 3"
    DEMO_MODEL_4 = "Demo Model 4"
    DEMO_MODEL_5 = "Demo Model 5"
    DEMO_MODEL_DEFAULT = "Demo Model Default"

class ManufacturerChoices(models.TextChoices):
    MN_MODEL_1 = "Manufacturer Model 1"
    MN_MODEL_2 = "Manufacturer Model 2"
    MN_MODEL_3 = "Manufacturer Model 3"
    MN_MODEL_4 = "Manufacturer Model 4"
    MN_MODEL_5 = "Manufacturer Model 5"
    MN_MODEL_DEFAULT = "Manufacturer Model Default"

class ColorChoices(models.TextChoices):
    COLOR_1 = "Color 1"
    COLOR_2 = "Color 2"
    COLOR_DEFAULT = "Color Default"
