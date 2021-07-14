from typing import List, Optional

from fastapi import HTTPException

from db.db import db
from models.departamentos import Departamentos
from repository.departamentos_repository import DepartamentoRepository
from repository.provicias_repository import ProvinciaRepository


class DepartamentoService:

    @classmethod
    def get_all(cls) -> List[Departamentos]:
        return DepartamentoRepository.get_departamentos()

    @classmethod
    def get_one(cls, id: int) -> Optional[Departamentos]:
        cls.validate_depart_id(id)
        return DepartamentoRepository.get_departamento(id)

    @classmethod
    def get_all_from_province(cls, province_id: int) -> List[Departamentos]:
        cls.validate_province(province_id)
        return DepartamentoRepository.get_all_from_province(province_id)

    @classmethod
    def put_departamento(cls, data: dict, id: int) -> Optional[Departamentos]:
        depart = DepartamentoRepository.get_departamento(id)

        if not depart:
            raise HTTPException(status_code=400, detail='Bad ID')

        cls.validate_province(province_id=data['provincia_id'])

        depart.nombre = data.get('nombre', depart.nombre)
        depart.provincia_id = data.get('provincia_id', depart.provincia_id)

        db.commit()
        return depart

    @classmethod
    def post_departamento(cls, data: dict) -> Optional[Departamentos]:
        cls.validate_new_depart_id(data.get('id'))

        cls.validate_province(province_id=data['provincia_id'])

        depart = Departamentos(
            id=data['id'],
            provincia_id=data['provincia_id'],
            nombre=data['nombre']
        )
        db.add(depart)
        db.commit()
        return depart

    @classmethod
    def validate_province(cls, province_id: int) -> None:
        if not ProvinciaRepository.validate_provincia_id(province_id):
            raise HTTPException(status_code=400,
                                detail="Bad provincia_id, no exist")

    @classmethod
    def validate_new_depart_id(cls, _id: int) -> None:
        if DepartamentoRepository.validate_depart_id(_id):
            raise HTTPException(status_code=400, detail='ID in use')

    @classmethod
    def validate_depart_id(cls, _id: int) -> None:
        if not DepartamentoRepository.validate_depart_id(_id):
            raise HTTPException(status_code=400, detail='Bad id')
