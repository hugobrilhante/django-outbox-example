from functools import partial

from django.contrib.auth.models import AbstractUser
from src.apps.outbox.models import with_outbox


@with_outbox("/topic/VirtualTopic.user-created")
class User(AbstractUser):
    pass
