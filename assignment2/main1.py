from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    userid: int
    username: str
    password: str
    email: str
    isadmin: bool
    isreporter: bool
    isanalyst: bool
    isviewer:bool


users = {
    "1": User(userid=1,username="fakeuser1",password="fakepassword1",email="fake1@email.com",isadmin=True,isreporter=True,isanalyst=False,isviewer=True),
    "2": User(userid=1,username="fakeuser2",password="fakepassword2",email="fake2@email.com",isadmin=False,isreporter=False,isanalyst=False,isviewer=True),
    "3": User(userid=1,username="fakeuser3",password="fakepassword3",email="fake3@email.com",isadmin=False,isreporter=True,isanalyst=False,isviewer=True),
    "4": User(userid=1,username="fakeuser4",password="fakepassword4",email="fake4@email.com",isadmin=False,isreporter=False,isanalyst=False,isviewer=True),
}

@app.get("/")
def read_root():
    return {"I left everything I own in One Piece": "Now you just have to find it."}

# GET /users : Return a list of all known users
@app.get("/users")
def get_all_users():
    return users

# GET /users/{user_id} : Return information for a specific user 
@app.get("/users/{user_id}")
def read_item(user_id: int):
    return {"user_id": user_id, "user": users[str(user_id)]}

# PUT /users/{user_id} : Update user info for a specific user
@app.put("/users/{user_id}")
def update_item(user_id: int, user: User):
    users[str(user_id)] = user
    return {"user_id": user_id, "users": users[str(user_id)]}

# PUT /users/add/{user_id} : Add a new user
@app.post("/users/add/{user_id}") 
def add_item(user_id: int, user: User):
    users[str(user_id)] = user
    return {"user_id": user_id, "users": users[str(user_id)]}

# PUT /users/delete/{user_id} : Add a new user
@app.delete("/users/delete/{user_id}")
def delete_user(user_id:int, user: User):
    global users
    user = [user for user in users if user.user_id != user_id]
    return {"message": f"User {user_id} deleted successfully"}