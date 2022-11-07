from starlette.routing import Mount
from MyListAnalyzerAPI.routes import my_list_analyzer


app_router = Mount(
    "/", routes=[
        my_list_analyzer
    ]
)
