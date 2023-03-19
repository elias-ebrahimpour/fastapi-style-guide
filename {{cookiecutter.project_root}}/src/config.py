import uvicorn
from fastapi import FastAPI


def start(*, app:FastAPI, host:str = "127.0.0.1", port:int = 5000):
    uvicorn.run(app=app, host=host, port=port)