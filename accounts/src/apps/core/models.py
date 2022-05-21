from django.contrib.auth.models import AbstractUser
from django_stomp.builder import build_publisher


class User(AbstractUser):

    def save(self, *args, **kwargs):
        publisher = build_publisher()
        publisher.send(queue="/topic/VirtualTopic.user-created",
                       body={"description": f"Recommendation to {self.username}"})
        super().save(*args, **kwargs)
