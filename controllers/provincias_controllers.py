from fastapi import APIRouter
from starlette import status

from schemas.provincias_schemas import ProvinciaSchema, ResponseGetAllSchemas
from services.provincia_services import \
    Provincias_Services as provincia_service

router = APIRouter()


@router.get("",
            name="Provincias",
            status_code=status.HTTP_200_OK,
            response_model=ResponseGetAllSchemas)
async def get():
    return provincia_service.get_all()


@router.get("/{id}",
            name="Provincia por Id",
            status_code=status.HTTP_200_OK,
            response_model=ProvinciaSchema)
async def get_one(id):
    return provincia_service.get_one(id)
