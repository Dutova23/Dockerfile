from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root_action():
    return {"surname": "Дутова", "name": "Анна", "patronymic": "Александровна"}

@app.get("/users")
def users_action():
    return {"phone_number": "899339320842", "email": "dutovaania@gmail.com"}

@app.get("/tools")
def users_action():
    return {"info": "Сделать простое API, используя FastAPI и Docker"}
