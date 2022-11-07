import uvicorn

if __name__ == "__main__":
    uvicorn.run("api.index:app", reload=True, port=6966, host="127.0.0.1")
