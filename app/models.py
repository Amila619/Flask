from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    description = Column(String, nullable = False)
    price = Column(Integer, nullable = False)
    active = Column(Boolean, server_default = 'TRUE')
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}