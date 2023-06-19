from pydantic import BaseModel, Field


class StoreModel(BaseModel):
    name: str = Field()
    source: str = Field()
    notes: str = Field()  
    cookie: str = Field()
    email: str = Field()
    created_time: int | None = Field()


class DoubanModel(BaseModel):
    douban_id: str = Field()
    douban_uid: str = Field()
    wish: str = Field()
    do: str = Field()
    collect: str = Field()
    join_time: int = Field()

class StoreRecordModel(BaseModel):
    token: str = Field()
    created_time: int = Field()


class MovieStatsModel(BaseModel):
    country: str = Field()
    genre: str = Field()
    year: str = Field()
    rating: str = Field()
    duration: str = Field()
    lan: str = Field()
    word: str = Field()

