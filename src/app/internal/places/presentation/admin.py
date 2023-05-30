from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.internal.places.db.models import Place

from django_admin_geomap import ModelAdmin


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"

    geomap_default_longitude = "95.1849"
    geomap_default_latitude = "64.2637"
    geomap_default_zoom = "3"

    geomap_item_zoom = "10"
    geomap_height = "300px"