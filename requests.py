from pydantic import BaseModel


class UserTokenRequest(BaseModel):
    username: str
    password: str


class AnonymizeRequest(BaseModel):
    password: str
    data: dict
