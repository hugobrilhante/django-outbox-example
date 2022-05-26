from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Published
from .models import Received

admin.site.register(Published, ModelAdmin, **{"list_display": ("name", "content", "status")})
admin.site.register(Received, ModelAdmin, **{"list_display": ("name", "content", "status")})
