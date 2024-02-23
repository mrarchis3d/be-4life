from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(
        ...,
        min_length=4, 
        max_length=50, 
        example="4Life Riovida")
    shortDescription: str = Field(
        ...,
        min_length=4, 
        max_length=1000, 
        example="el mejor producto")
    longDescription: str
    price: int 
    prevPrice: int
    saving: int
    url: str = Field(
        ...,
        min_length=4, 
        max_length=250, 
        example="https://wa.me/...")
    image: str = Field(
        ...,
        min_length=4, 
        max_length=50, 
        example="image.png")

    
class ProductCreated(ProductBase):
    id:str