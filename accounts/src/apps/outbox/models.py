import json

from django.core import serializers
from django.db import models
from django.db import transaction


class Outbox(models.Model):
    queue = models.CharField(max_length=100)
    body = models.JSONField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.queue} - {self.body}"


def with_outbox(queue, fields=None):
    def save(self, *args, **kwargs):
        with transaction.atomic():
            super(self.__class__, self).save(*args, **kwargs)
            data = serializers.serialize("json", [self], fields=fields)
            outbox = Outbox(
                queue=queue,
                body=json.loads(data)
            )
            outbox.save()

    def decorator_with_outbox(cls):
        cls.save = save
        return cls

    return decorator_with_outbox
