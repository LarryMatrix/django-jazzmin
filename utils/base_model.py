import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          unique=True, editable=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(
        'Deleted Date', auto_now=True, auto_now_add=False)
    deleted_by = models.CharField(
        max_length=255, null=True, blank=True, default=None)

    class Meta:
        abstract = True
