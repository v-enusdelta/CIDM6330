from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import UserPayload

#This variable has been intentionally broken to use the test folder instead. To fix it, remove '1' from the variable name.
app1 = FastAPI()

user_list: dict[int, UserPayload] = {}

# GET / :Initial system message
@app.get("/")
def read_root() -> dict[str, str]:
    return {"message":"System available"}

# GET /users: Returns a list of all known users
@app.get("/users")
def get_all_users() -> dict[int, UserPayload]:
    return user_list

# POST /users/add: Add a new user
def add_user():
    