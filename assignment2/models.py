from typing import Optional, Union
from pydantic import BaseModel

#Create a Pydantic model for a User class

class UserPayload(BaseModel):
    username: str
    userpassword: str
    isadmin: bool