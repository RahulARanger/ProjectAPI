from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


def get_cors():
    origins = [
        "https://rahularanger.vercel.app",
        "https://rahularanger-fe-rahularanger.vercel.app",
        "https://rahularanger-fe-git-master-rahularanger.vercel.app"
    ]
    return Middleware(
        CORSMiddleware, allow_origins=origins,
        allow_methods=["*"], allow_headers=["*"], allow_credentials=True
    )


def config_server(*mounts):
    return Starlette(
        debug=False,
        middleware=[
            get_cors()
        ],
        routes=mounts
    )
