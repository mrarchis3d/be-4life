from typing import List, Optional

from fastapi import Depends
from app.models.ProductModel import Product

from app.repositories import ProductRepository
from app.schemas import ProductSchema



class ProductService:
    authorRepository: ProductRepository

    def __init__(
        self, authorRepository: ProductRepository = Depends()
    ) -> None:
        self.authorRepository = authorRepository

    def create(self, author_body: ProductSchema) -> Product:
        return self.authorRepository.create(
            Product(name=author_body.name)
        )

    def delete(self, author_id: int) -> None:
        return self.authorRepository.delete(
            Product(id=author_id)
        )

    def get(self, author_id: int) -> Product:
        return self.authorRepository.get(
            Product(id=author_id)
        )

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Product]:
        return self.authorRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, author_id: int, author_body: ProductSchema
    ) -> Product:
        return self.authorRepository.update(
            author_id, Product(name=author_body.name)
        )

    def get_products(self, author_id: int) -> List[Product]:
        return self.authorRepository.get(
            Product(id=author_id)
        ).products