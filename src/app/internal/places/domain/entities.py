from ninja import Schema


class PlaceSchema(Schema):
    name: str
    description: str
    lon: float
    lat: float


class PlaceOut(PlaceSchema):
    id: int


class PlaceIn(PlaceSchema):
    ...
