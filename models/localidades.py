from sqlalchemy import Column, Integer

from db.db import Base


class Localidades(Base):
    __tablename__ = "localidades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(Integer, unique=True, index=True)
    departamento_id = Column(Integer, index=True)
