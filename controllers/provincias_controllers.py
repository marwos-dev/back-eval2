from fastapi import APIRouter, Response, HTTPException
from starlette import status
from models.provincias import Provincias
from schemas.provincias_schemas import ProvinciaSchema, ProvinciasSchemaSimple
from services.provincia_services import Provincias_Services as provincia_service
from fastapi_pagination import Page, paginate

router = APIRouter()


@router.get("", name="Provincias", status_code=status.HTTP_200_OK)
async def get():
    return provincia_service.get_all()


@router.get("/{id}", name="Provincia por Id", status_code=status.HTTP_200_OK, response_model=ProvinciaSchema)
async def get_one(id):
    return provincia_service.get_one(id)


