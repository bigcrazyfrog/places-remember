from django.db import models
from django_admin_geomap import GeoItem


class Place(models.Model, GeoItem):
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)

    # coordinates
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    owner = models.ForeignKey("AdminUser", on_delete=models.CASCADE)

    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)

    @property
    def geomap_icon(self):
        return self.default_icon

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
