# app/models/category.py

from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    menu_nm = Column(String, index=True, nullable=False)
    menu_cd = Column(String, index=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    type = Column(String, index=True, nullable=False)