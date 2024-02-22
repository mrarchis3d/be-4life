

from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    shortDescription: str
    longDescription: str
    price: int
    prevPrice: int
    saving: int
    url: str
    image: str