from fastapi import APIRouter
from starlette import status

from schemas.departamentos_schemas import DepartamentoSchema, \
    DepartamentosSchemaSimple, ResponseGetAllSchemas
from services.departamentos_service import DepartamentoService

router = APIRouter()


@router.get("",
            name="Departamentos",
            status_code=status.HTTP_200_OK,
            response_model=ResponseGetAllSchemas)
async def get():
    return {'data': DepartamentoService.get_all()}


@router.get("/province/{province_id}",
            name="Departamentos",
            status_code=status.HTTP_200_OK,
            response_model=ResponseGetAllSchemas)
async def get_all_from_province(province_id: int):
    return {
        'data': DepartamentoService.get_all_from_province(
            province_id=province_id)
    }


@router.get("/{id}",
            name="Departamento por Id",
            status_code=status.HTTP_200_OK,
            response_model=DepartamentoSchema)
async def get_one(id):
    return DepartamentoService.get_one(id)


@router.put("/{id}",
            name="Editar departamento",
            status_code=status.HTTP_200_OK,
            response_model=DepartamentoSchema)
async def update_departament(id: int, data: DepartamentosSchemaSimple):
    return DepartamentoService.put_departamento(data=data.dict(), id=id)


@router.post("",
             name="Crear un departamento",
             status_code=status.HTTP_201_CREATED,
             response_model=DepartamentoSchema)
async def post_departamento(data: DepartamentoSchema):
    return DepartamentoService.post_departamento(data=data.dict())
