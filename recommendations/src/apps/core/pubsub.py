import logging

from django_stomp.services.consumer import Payload

from .models import Recommendation

logger = logging.getLogger(__name__)


def create_recommendation(payload: Payload) -> None:
    if payload.body.get("description"):
        Recommendation.objects.get_or_create(**payload.body)
        payload.ack()
    else:
        logger.info("To DLQ!")
        payload.nack()
