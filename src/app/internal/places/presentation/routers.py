from django.urls import path

from app.internal.places.presentation.views import PlaceViews


def get_place_urls(place_views: PlaceViews):
    urls = [
        path('', place_views.view_places),
        path('<int:id>/', place_views.view_place_by_id),
        path('add/', place_views.add_place_form),
    ]

    return urls
