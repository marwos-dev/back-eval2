from contextlib import AbstractContextManager
from typing import Callable
from typing import List, Optional

from sqlalchemy.orm import Session

from db.db import db
from models.departamentos import Departamentos


class DepartamentoRepository:

    @classmethod
    def get_departamentos(cls) -> List[Departamentos]:
        return db.query(Departamentos).all()

    @classmethod
    def get_departamento(cls, _id: int) -> Optional[Departamentos]:
        return db.query(Departamentos).filter(Departamentos.id == _id).first()

    @classmethod
    def get_all_from_province(cls, province_id: int) -> List[Departamentos]:
        return db.query(Departamentos).filter(
            province_id == Departamentos.provincia_id
        ).all()

    @classmethod
    def validate_depart_id(cls, _id: int) -> bool:
        return db.query(Departamentos).filter(
            _id == Departamentos.id
        ).count() >= 1
