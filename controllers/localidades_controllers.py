from fastapi import APIRouter
from starlette import status

from schemas.localidades_schemas import LocalidadesSchema, \
    LocalidadesSchemaSimple
from services.localidades_service import LocalidadesService
from fastapi_pagination import Page, paginate

router = APIRouter()


@router.get("",
            name="Localidades",
            status_code=status.HTTP_200_OK)
async def get():
    return LocalidadesService.get_all()


@router.get("/departamento/{departamento_id}",
            name="Localidades de un departamento",
            status_code=status.HTTP_200_OK)
async def get_all_from_departament(departament_id: int):
    return LocalidadesService.get_all_from_departament(
        departament_id=departament_id
    )


@router.get("/{id}",
            name="Localidades por Id",
            status_code=status.HTTP_200_OK,
            response_model=LocalidadesSchema)
async def get_one(id: int):
    return LocalidadesService.get_one(id)


@router.put("/{id}",
            name="Editar localidad",
            status_code=status.HTTP_200_OK,
            response_model=LocalidadesSchema)
async def update_departament(id: int, data: LocalidadesSchemaSimple):
    return LocalidadesService.put_departamento(data=data.dict(), id=id)


@router.post("",
             name="Crear una localidad",
             status_code=status.HTTP_201_CREATED,
             response_model=LocalidadesSchema)
async def post(data: LocalidadesSchema):
    return LocalidadesService.post_localidad(data=data.dict())
