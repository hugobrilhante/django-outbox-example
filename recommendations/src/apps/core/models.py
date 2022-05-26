from django.db import models


class Recommendation(models.Model):
    content = models.JSONField()

    def __str__(self):
        return f"{self.content}"