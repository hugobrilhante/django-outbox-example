from django.db import models


class Outbox(models.Model):
    queue = models.CharField(max_length=100)
    body = models.JSONField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.queue} - {self.body}"
