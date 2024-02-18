from django.contrib import admin
from django.contrib.admin import ModelAdmin

from src.apps.users.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        None,
        {"classes": ("wide",), "fields": ("email", "password1", "password2", "is_staff", "is_active")},
    )
    search_fields = ("email",)
    ordering = ("email",)
