from django.contrib import admin
from django.contrib.admin import ModelAdmin

from src.apps.events.models import Event


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ("title", "date", "location", "organizer")
    list_filter = ("title", "date", "location", "organizer")
    fields = ("title", "description", "date", "location", "organizer", "participants")
