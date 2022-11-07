from starlette.applications import Starlette
from api.build import config_server
from api.routes import app_router

app: Starlette = config_server(app_router)

