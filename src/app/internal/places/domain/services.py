from typing import List

from app.internal.places.domain.entities import PlaceOut


class IPlaceRepository:
    def get_place_by_id(self, id: int, user_id: str) -> PlaceOut:
        ...

    def get_places(self, user: str) -> List[PlaceOut]:
        ...


class PlaceService:
    def __init__(self, place_repo: IPlaceRepository):
        self._place_repo = place_repo

    def get_place_by_id(self, id: int, user_id: str) -> PlaceOut:
        return self._place_repo.get_place_by_id(id=id, user_id=user_id)

    def get_places(self, user: str) -> List[PlaceOut]:
        return self._place_repo.get_places(user=user)
