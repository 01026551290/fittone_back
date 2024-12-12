# app/api/v1/endpoints/categories.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.schemas.category import CategoryCreate, CategoryResponse
from app.models.category import Category
from app.db.session import get_db

router = APIRouter(
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    # 카테고리 이름 중복 확인
    result = await db.execute(select(Category).where(Category.name == category.name))
    existing_category = result.scalars().first()
    if existing_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    new_category = Category(
        menu_nm=category.menu_nm,
        menu_cd=category.menu_cd,
        created_at=category.created_at
    )
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category

@router.get("/", response_model=List[CategoryResponse])
async def read_categories(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category).offset(skip).limit(limit))
    categories = result.scalars().all()
    return categories

@router.get("/{menu_cd}", response_model=CategoryResponse)
async def read_category(menu_cd: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category).where(Category.menu_cd == menu_cd))
    category = result.scalars().first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.get("/type/{type}", response_model=List[CategoryResponse])
async def read_category_type(type: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category).where(Category.type == type))
    categories = result.scalars().all()
    return categories
    
