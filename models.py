from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId


class User(BaseModel):
    username: str
    hashed_password: str
    data: dict


class UserInDB(User):
    _id: ObjectId
    date_created: datetime = Field(default_factory=datetime.utcnow)


class De_Anon(BaseModel):
    user: UserInDB
    connector_id: ObjectId
    content: str = None


class De_AnonInDB(De_Anon):
    _id: ObjectId
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
