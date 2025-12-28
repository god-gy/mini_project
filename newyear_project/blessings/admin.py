# blessings/admin.py
from django.contrib import admin
from .models import PresetBlessing, UserBlessing

@admin.register(PresetBlessing)
class PresetBlessingAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active", "created_at", "content")
    list_filter = ("is_active",)
    search_fields = ("content",)

@admin.register(UserBlessing)
class UserBlessingAdmin(admin.ModelAdmin):
    list_display = ("id", "from_email", "created_at")
    search_fields = ("from_email", "message")
    list_filter = ("created_at",)
