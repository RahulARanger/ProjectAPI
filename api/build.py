from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


def get_cors():
    origins = [
        "http://127.0.0.1:6969"
    ]
    return Middleware(
        CORSMiddleware, allow_origins=origins
    )


def config_server(*mounts):
    return Starlette(
        debug=False,
        middleware=[
            get_cors()
        ],
        routes=mounts
    )
