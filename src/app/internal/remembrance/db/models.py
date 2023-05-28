import uuid

from django.db import models


class Place(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, default=None)
    description = models.CharField(max_length=255, default=None)

    # coordinates
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    owner = models.ForeignKey("AdminUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
