from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
from fastapi.requests import Request
from api import __version__

server = FastAPI(
    title="Project-API",
    description="Just Provides Some backend support for my projects",
    version=__version__,
    contact={
        "name": "RahulARanger",
        "email": "saihanumarahul66@gmail.com"
    }
)


@server.route("/")
def greet(_: Request) -> PlainTextResponse:
    return PlainTextResponse(content="Hello, There", status_code=200)


@server.exception_handler(404)
async def explain_routes(_, __):
    return PlainTextResponse(
        content="Please refer to other routes, as this one was not implemented yet", status_code=404)


config = uvicorn.Config("index:server", port=6966)
app = uvicorn.Server(config)

if __name__ == '__main__':
    app.run()
