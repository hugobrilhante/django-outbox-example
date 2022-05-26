import logging

from django_stomp.services.consumer import Payload

from .models import Recommendation

logger = logging.getLogger(__name__)


def create_recommendation(payload: Payload) -> None:
    if payload.body.get("pk"):
        Recommendation.objects.get_or_create(content=payload.body)
        payload.ack()
