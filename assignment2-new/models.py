from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    userid: Optional[int]
    username: str
    password: int
    email: str
    isadmin: bool
    isreporter: bool
    isanalyst: bool
    isviewer:bool