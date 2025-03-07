# Updates
3/7/25 Note: The codeblock in the FastAPI section has been updated with main.py from /assignment2-new
# ERD
The following ERD captures the relationships between a user class, their roles and permissions, and how they interact with the item class.

Items are text-heavy objects that generally correlate to a focus issue in the agency strategic plan. Items can be goals, objectives, strategies, tactics, or metrics. As such, they require periodic updates to their status (completed, incomplete, etc.), a value for a tracking metric (and their corresponding data type), and any relevant comments. Considerable metadata are attached to these items as well such as who they are assigned to, who created them, when they were created, and when they were last updated. A key aspect of items is knowing their history. This information is captured in the ItemHistory table, modeled after a periodic snapshot schema, but contains considerable hybrid elements.

Users interact with items through Events, which provide a layer of abstraction and serve as a control mechanism to organize what type of change was made to the item, if at all. The Event module also needs to verify that a particular user has permission to participate in the type of event (create, read, update, delete, etc.). Although this is not explicitly described in the ERD below, it is implied through the dashed box.


![ERD for users and items](/assignment2/class-erd.png)

# FastAPI

All final code is contained in the following path CIDM6330/assignment2-new/main.py and executed with the command `uvicode main:app --reload` in Git Bash

This code focuses on CRUD operations relevant to the User class.

```python
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
```