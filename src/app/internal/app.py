from django.urls import path, include

from app.internal.places.db.repositories import PlaceRepository
from app.internal.places.domain.services import PlaceService
from app.internal.places.presentation.routers import get_place_urls
from app.internal.places.presentation.views import PlaceViews


def get_urls():
    place_repo = PlaceRepository()
    place_service = PlaceService(place_repo=place_repo)
    place_views = PlaceViews(place_service=place_service)
    place_urls = get_place_urls(place_views=place_views)

    urls = [
        path('places/', include(place_urls)),
    ]

    return urls


urls = get_urls()
