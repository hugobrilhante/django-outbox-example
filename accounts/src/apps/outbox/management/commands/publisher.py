from time import sleep

from django.core.management.base import BaseCommand
from django.db import DatabaseError
from django_stomp.builder import build_publisher
from src.apps.core.models import Outbox


class Command(BaseCommand):
    help = "Sending outbox messages"

    def handle(self, *args, **options):
        started = False
        publisher = build_publisher()
        while True:
            try:
                outboxes = Outbox.objects.filter(sent=False)
                for outbox in outboxes:
                    publisher.send(queue=outbox.queue, body=outbox.body)
                    outbox.sent = True
                    outbox.save()
                    self.stdout.write(self.style.SUCCESS(f"{outbox.body} published"))
            except DatabaseError:
                self.stdout.write(self.style.SUCCESS(f"Starting publisher..."))
            else:
                if not started:
                    self.stdout.write(self.style.SUCCESS(f"Publisher started!"))
                    started = True
            sleep(1)
