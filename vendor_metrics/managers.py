import datetime
from django.db import models
from .queryset import BaseModelQuerySet

class BaseModelManager(models.Manager):

    def get_queryset(self):
        query = BaseModelQuerySet(self.model, using=self._db)
        return query

    def update(self, payload, **kwargs):
        return self.get_queryset().update(**kwargs)