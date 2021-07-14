from sqlalchemy import Column, Integer

from db.db import Base


class Departamentos(Base):
    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(Integer, unique=True, index=True)
    provincia_id = Column(Integer, index=True)
