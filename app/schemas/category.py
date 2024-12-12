 # app/schemas/category.py

from pydantic import BaseModel
from datetime import datetime

class CategoryBase(BaseModel):
    menu_nm: str
    menu_cd: str
    created_at: datetime

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True  # SQLAlchemy 모델과 매핑을 위해 설정