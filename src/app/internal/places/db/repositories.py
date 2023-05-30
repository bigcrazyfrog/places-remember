from typing import List
from uuid import UUID

from app.internal.places.db.exceptions import NotFoundException
from app.internal.places.domain.entities import PlaceOut
from app.internal.places.domain.services import IPlaceRepository
from app.internal.places.db.models import Place


class PlaceRepository(IPlaceRepository):
    def get_place_by_id(self, id: int, user_id: str) -> PlaceOut:
        place = Place.objects.filter(id=id, owner__id=user_id).first()
        if place is None:
            raise NotFoundException(name="Place", id=str(id))

        return PlaceOut.from_orm(place)

    def get_places(self, user: str) -> List[PlaceOut]:
        return Place.objects.filter(owner=user)
