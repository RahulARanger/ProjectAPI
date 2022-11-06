from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
from fastapi.requests import Request
from api import __version__
from fastapi.middleware.cors import CORSMiddleware
from api.Parts import application_router

app = FastAPI(
    title="Project-API",
    description="Just Provides Some backend support for my projects",
    version=__version__,
    contact={
        "name": "RahulARanger",
        "email": "saihanumarahul66@gmail.com"
    }
)

origins = [
    "https://rahularanger-fe-git-master-rahularanger.vercel.app/",
    "https://rahularanger.vercel.app/",
    "https://rahularanger-fe-rahularanger.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(application_router)


@app.route("/")
def greet(_: Request) -> PlainTextResponse:
    return PlainTextResponse(content="Hello, There", status_code=200)


@app.exception_handler(404)
async def explain_routes(_, __):
    return PlainTextResponse(
        content="Please refer to other routes, as this one was not implemented yet", status_code=404)


config = uvicorn.Config("api.index:app", port=6966)
server = uvicorn.Server(config)
