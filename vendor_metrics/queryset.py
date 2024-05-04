
from django.db import models
from django.utils import timezone


class BaseModelQuerySet(models.QuerySet):

    def update(self, **kwargs):
        kwargs.update(updated=timezone.now())
        return super().update(**kwargs)