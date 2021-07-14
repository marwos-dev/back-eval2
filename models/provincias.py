from sqlalchemy import Column, Integer

from db.db import Base


class Provincias(Base):
    __tablename__ = "provincias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(Integer, unique=True, index=True)
