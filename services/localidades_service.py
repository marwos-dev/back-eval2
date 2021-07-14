from typing import List, Optional

from fastapi import HTTPException

from db.db import db
from models.localidades import Localidades
from repository.departamentos_repository import DepartamentoRepository
from repository.localidades_repository import LocalidadesRepository


class LocalidadesService:

    @classmethod
    def get_all(cls) -> List[Localidades]:
        return LocalidadesRepository.get_localidades()

    @classmethod
    def get_one(cls, id: int) -> Optional[Localidades]:
        cls.validate_localidad_id(id)
        return LocalidadesRepository.get_localidad(id)

    @classmethod
    def get_all_from_departament(cls, departament_id: int) -> List[
        Localidades]:
        cls.validate_departamento(departament_id)
        return LocalidadesRepository.get_all_from_departamento(departament_id)

    @classmethod
    def put_departamento(cls, data: dict, id: int) -> Optional[Localidades]:
        localidad = LocalidadesRepository.get_localidad(id)

        if not localidad:
            raise HTTPException(status_code=400, detail='Bad ID')

        cls.validate_departamento(departamento_id=data['departamento_id'])

        localidad.nombre = data.get('nombre', localidad.nombre)
        localidad.provincia_id = data.get('provincia_id',
                                          localidad.departamento_id)

        db.commit()
        return localidad

    @classmethod
    def post_localidad(cls, data: dict) -> Optional[Localidades]:
        cls.validate_new_localidad_id(data.get('id'))

        cls.validate_departamento(departamento_id=data['departamento_id'])

        localidad = Localidades(
            id=data['id'],
            departamento_id=data['departamento_id'],
            nombre=data['nombre']
        )
        db.add(localidad)
        db.commit()
        return localidad

    @classmethod
    def validate_departamento(cls, departamento_id: int) -> None:
        if not DepartamentoRepository.validate_depart_id(departamento_id):
            raise HTTPException(status_code=400,
                                detail="Bad departamento_id, no exist")

    @classmethod
    def validate_new_localidad_id(cls, _id: int) -> None:
        if LocalidadesRepository.validate_local_id(_id):
            raise HTTPException(status_code=400, detail='ID in use')

    @classmethod
    def validate_localidad_id(cls, _id: int) -> None:
        if not LocalidadesRepository.validate_local_id(_id):
            raise HTTPException(status_code=400, detail='Bad id')
