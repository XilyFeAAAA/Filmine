from pydantic import BaseModel, Field


class NewUserModel(BaseModel):
    username: str = Field()
    email: str = Field()
    password: str = Field(default='sa')

class SafeUserModel(BaseModel):
    username: str = Field()
    email: str = Field()


class VerifyModel(BaseModel):
    token: str = Field()
    email: str = Field()
    state: bool = Field()