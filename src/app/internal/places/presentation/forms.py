from django import forms

from app.internal.places.db.models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'description', 'lon', 'lat')
