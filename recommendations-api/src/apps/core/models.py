from django.db import models


class Recommendation(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"
