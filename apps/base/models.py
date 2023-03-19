import uuid
from django.db import models


class TimeStampedModel(models.Model):
    """Abstract model with created at and modified at timestamps
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # this is an abstract model


class UUIDTimeStampedModel(TimeStampedModel):
    '''
    Base model that stores created_at, modified_at, and id (which is
    a uuid string).
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True  # this is an abstract model