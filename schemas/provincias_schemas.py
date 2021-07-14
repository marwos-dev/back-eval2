from typing import List

from pydantic import BaseModel


class ProvinciaSchema(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True


class ProvinciasSchemaSimple(BaseModel):
    nombre: str
   
    class Config:
        orm_mode = True


class ResponseGetAllSchemas(BaseModel):
    data: List[ProvinciaSchema]
