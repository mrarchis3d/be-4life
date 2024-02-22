from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    DateTime,
    func,
    PrimaryKeyConstraint,
    String,
)

Base = declarative_base()
metadata = Base.metadata


class Product(Base):
    __tablename__ = "products"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    shortDescription = Column(String(1000), nullable=False)
    longDescription = Column(String, nullable=False)
    isActive = Column(Boolean, nullable=False, default=True)
    price=Column(Integer, nullable=False)
    prevPrice=Column(Integer, nullable=False)
    saving=Column(Integer, nullable=False)
    url = Column(String(250), nullable=False)
    image = Column(String(50), nullable=False)
    createdAt = Column(DateTime, nullable=False, default=func.now())
    updatedAt = Column(DateTime, nullable=False, default=func.now(), onupdate=datetime.now)
    removedAt = Column(DateTime, nullable=False, default=None)


    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
        }