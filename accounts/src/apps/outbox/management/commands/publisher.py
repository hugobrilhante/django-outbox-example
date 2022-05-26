from time import sleep

from django.core.management.base import BaseCommand
from django.db import DatabaseError
from django_stomp.builder import build_publisher
from src.apps.outbox.models import Published
from src.apps.outbox.models import StatusChoice


class Command(BaseCommand):
    help = "Sending outbox messages"

    def handle(self, *args, **options):
        started = False
        publisher = build_publisher()
        while True:
            try:
                published = Published.objects.filter(status=StatusChoice.SCHEDULE)
                for pub in published:
                    publisher.send(queue=pub.name, body=pub.content)
                    pub.status = StatusChoice.SUCCEEDED
                    pub.save()
                    self.stdout.write(self.style.SUCCESS(f"{pub.content} published"))
            except DatabaseError:
                self.stdout.write(self.style.SUCCESS(f"Starting publisher..."))
            else:
                if not started:
                    self.stdout.write(self.style.SUCCESS(f"Publisher started!"))
                    started = True
            sleep(1)
