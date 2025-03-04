from fastapi import FastAPI, HTTPException

from models import User

app = FastAPI()

user_list: dict[int, User] = {}

@app.get ("/")
def read_root():
    return {"Message": "System initialized"}

# POST /users/{username} : Add a new user
@app.post("/users/{username}")
def add_user(username: str, user: User) -> dict[str, User]:
    existing_usernames = {user.username for user in user_list.values()}
    if username in existing_usernames:
        raise HTTPException(status_code=400, detail="Username already taken.")

    # Generate a unique user_id
    user_id = max(user_list.keys(), default=0) + 1 if user_list else 0

    # Create a new User object
    new_user = User(userid=userid, username=username, password=password, email=email, isadmin=isadmin, isreporter=isreporter, isanalyst=isanalyst, isviewer=isviewer)

    # Add the new user to user_list
    user_list[user_id] = new_user

    return {"user": new_user}

# GET /users/{user_id} : Return user information by user_id
@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, User]:
    if user_id not in user_list:
        raise HTTPException(status_code=404, detail="UserID not found.")
    return {"item": user_list[user_id]}

# PUT /users/{user_id} : Update user info for a specific user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User) -> dict[str, User]:
    if user_id not in user_list:
        raise HTTPException(status_code=404, detail="UserID not found.")
    user_list[user_id] = user
    return {"user": user_list[user_id]}

# GET /users : Return a list of all users and user information
@app.get("/users")
def list_users() -> dict[int, User]:
    return user_list

# DELETE /users/{username} : Deletes a user by their username
@app.delete("/users/{username}")
def delete_user(username: str) -> dict[str, str]:
    if username not in user_list:
        raise HTTPException(status_code=404, detail="Username not found.")
    del user_list[username]
    return {"result": "Username deleted."}