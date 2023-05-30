from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.internal.places.db.exceptions import NotFoundException
from app.internal.places.db.models import Place
from app.internal.places.domain.entities import PlaceIn
from app.internal.places.domain.services import PlaceService
from app.internal.places.presentation.forms import PlaceForm


class PlaceViews:
    def __init__(self, place_service: PlaceService):
        self._place_service = place_service

    def view_places(self, request):
        places = self._place_service.get_places(request.user.id)
        return render(request, 'app/places.html', {"places": places})

    def view_place_by_id(self, request, id: int):
        place = None
        status = 'OK'
        try:
            place = self._place_service.get_place_by_id(id=id, user_id=request.user.id)
        except NotFoundException:
            status = 'Not found'

        return render(request, 'app/place.html', {"status": status, "place": place})

    def add_place_form(self, request):
        if request.method == "POST":
            form = PlaceForm(request.POST)
            if form.is_valid():
                data = PlaceIn(
                    name=request.POST.get('name', ''),
                    description=request.POST.get('description', ''),
                    lon=request.POST.get('lon', ''),
                    lat=request.POST.get('lat', ''),
                )
                self._place_service.create_place(data, request.user)

                return HttpResponseRedirect("/places/")
        else:
            form = PlaceForm()

        return render(request, "app/form.html", {"form": form})
