from db.db import db
from models.provincias import Provincias


class ProvinciaRepository:

    @classmethod
    def get_provincias(cls):
        return db.query(Provincias).all()

    @classmethod
    def get_provincia(cls, _id: int):
        return db.query(Provincias).filter(Provincias.id == _id).first()

    @classmethod
    def validate_provincia_id(cls, _id: int) -> bool:
        return db.query(Provincias).filter(
            _id == Provincias.id
        ).count() >= 1
