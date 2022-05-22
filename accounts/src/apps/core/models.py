from django.contrib.auth.models import AbstractUser
from django.db import transaction

from src.apps.outbox.models import Outbox


class User(AbstractUser):

    def save(self, *args, **kwargs):
        with transaction.atomic():
            outbox = Outbox(
                queue="/topic/VirtualTopic.user-created",
                body={"description": f"Recommendation to {self.username}"}
            )
            outbox.save()
            super().save(*args, **kwargs)
