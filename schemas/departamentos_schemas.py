from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator, EmailStr
from validator.provincia_validator import Validador_Provincia


class DepartamentosSchemaSimple(BaseModel): # noqa
    nombre: str
    provincia_id: int

    class Config:
        orm_mode = True


class DepartamentoSchema(DepartamentosSchemaSimple): # noqa
    id: int

    class Config:
        orm_mode = True

