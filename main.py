import uvicorn
from fastapi import APIRouter, FastAPI

# Controladores
from controllers.departamentos_controllers import router as departamento_router
from controllers.localidades_controllers import router as localidade_router
from controllers.provincias_controllers import router as provincia_router

# Aplicacion
app = FastAPI()

# Rutas API
api_router = APIRouter()

# Provincias
app.include_router(provincia_router,
                   tags=["Provincia"],
                   prefix="/provincias")

# Departamentos
app.include_router(departamento_router,
                   tags=["Departamento"],
                   prefix="/departamentos")

# Localidades
app.include_router(localidade_router,
                   tags=["Localidades"],
                   prefix="/localidades")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
