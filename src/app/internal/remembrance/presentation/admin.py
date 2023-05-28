from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.internal.remembrance.db.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass
