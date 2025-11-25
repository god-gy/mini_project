from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
# from app.schemas.comment import CommentRead

# pydantic 으로 스키마를 만들어서 사용자의 입력을 받으면 입력값 검증을 할 수 있다

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1, max_length=100_000)

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = Field(default=None, min_length=1, max_length=100_000)

class PostRead(PostBase):
    id: int
    owner_id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    # comments: list[CommentRead] = []   # 🔁 중첩 스키마

    model_config = ConfigDict(from_attributes=True)
