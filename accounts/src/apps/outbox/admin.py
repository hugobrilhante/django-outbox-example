from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Outbox

admin.site.register(Outbox, ModelAdmin, **{"list_display": ("queue", "body", "sent")})
