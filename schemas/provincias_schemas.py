from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator, EmailStr
from validator.provincia_validator import Validador_Provincia


class ProvinciaSchema(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True


class ProvinciasSchemaSimple(BaseModel):
    nombre: str
   
    class Config:
        orm_mode = True
