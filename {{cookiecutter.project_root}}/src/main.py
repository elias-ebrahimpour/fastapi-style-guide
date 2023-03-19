from fastapi import FastAPI
from first.router import router as first_router
import config


app = FastAPI(
    title="{{cookiecutter.project_name}} API",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    description="{{cookiecutter.project_description}}",
    version="{{cookiecutter.version}}",
)


app.include_router(first_router)


config.start(app=app, host="127.0.0.1", port=8000)
