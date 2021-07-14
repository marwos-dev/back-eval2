from typing import List, Optional

from db.db import db
from models.localidades import Localidades


class LocalidadesRepository:

    @classmethod
    def get_localidades(cls) -> List[Localidades]:
        return db.query(Localidades).all()

    @classmethod
    def get_localidad(cls, _id: int) -> Optional[Localidades]:
        return db.query(Localidades).filter(Localidades.id == _id).first()

    @classmethod
    def get_all_from_departamento(cls, departamento_id: int) -> \
            List[Localidades]:
        return db.query(Localidades).filter(
            departamento_id == Localidades.departamento_id
        ).all()

    @classmethod
    def validate_local_id(cls, _id: int) -> bool:
        return db.query(Localidades).filter(
            _id == Localidades.id
        ).count() >= 1
