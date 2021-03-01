from pydantic import BaseModel


class UserTokenRequest(BaseModel):
    username: str
    password: str
