from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.ProductModel import Product

class ProductRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Product]:
        query = self.db.query(Product)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def get(self, id: str) -> Product:
        return self.db.get(
            Product,
            id,
            options=[lazyload(Product.books)],
        )

    def create(self, product: Product) -> Product:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update(self, id: int, product: Product) -> Product:
        product.id = id
        self.db.merge(product)
        self.db.commit()
        return product

    def delete(self, product: Product) -> None:
        self.db.delete(product)
        self.db.commit()
        self.db.flush()