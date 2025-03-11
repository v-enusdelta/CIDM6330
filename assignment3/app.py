from typing import Annotated, Sequence

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str
    email: str
    isadmin: bool 
    isreporter: bool
    isanalyst: bool
    isviewer:bool


sqlite_file_name = "userdb.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/users/")
def create_user(user: User, session:SessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.get("/users/")
def read_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users
   
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, session: SessionDep) -> User:
    user_db = session.get(User, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user_db.username = user.username
    user_db.password = user.password
    user_db.email = user.email
    user_db.isadmin = user.isadmin
    user_db.isreporter = user.isreporter
    user_db.isanalyst = user.isanalyst
    user_db.isviewer = user.isviewer
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db

@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"Mesage": "User {user_id} deleted successfully"}