import json
import uuid
from datetime import timedelta

from django.core import serializers
from django.db import models
from django.db import transaction
from django.utils import timezone


def _one_more_day():
    return timezone.now() + timedelta(1)


def with_outbox(name, fields=None):
    def save(self, *args, **kwargs):
        with transaction.atomic():
            super(self.__class__, self).save(*args, **kwargs)
            data = serializers.serialize("json", [self], fields=fields)
            outbox = Published(
                name=name,
                content=json.loads(data)[0]
            )
            outbox.save()

    def decorator_with_outbox(cls):
        cls.save = save
        return cls

    return decorator_with_outbox


class StatusChoice(models.IntegerChoices):
    FAILED = -1
    SCHEDULE = 1
    SUCCEEDED = 2


class Published(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="Id not sequential using UUID Field",
    )
    version = models.CharField(max_length=100, default='v1')
    name = models.CharField(max_length=100)
    content = models.JSONField()
    added = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=_one_more_day)
    retry = models.PositiveIntegerField(default=50)
    status = models.IntegerField(choices=StatusChoice.choices, default=StatusChoice.SCHEDULE)

    class Meta:
        verbose_name = 'published'

    def __str__(self):
        return f"{self.name} - {self.content}"

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.name = f"{self.name}.{self.version}"
        super().save(*args, **kwargs)


class Received(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="Id not sequential using UUID Field",
    )
    version = models.CharField(max_length=100, default='v1')
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100, null=True)
    content = models.JSONField()
    added = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=_one_more_day)
    retry = models.PositiveIntegerField(default=50)
    status = models.IntegerField(choices=StatusChoice.choices, default=StatusChoice.SCHEDULE)

    class Meta:
        verbose_name = 'received'

    def __str__(self):
        return f"{self.name} - {self.content}"

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.name = f"{self.name}.{self.version}"
        super().save(*args, **kwargs)
