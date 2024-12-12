from fastapi import FastAPI
from app.api import api_router
from app.db.base import Base
from app.db.session import engine

import asyncio

app = FastAPI(title="Health Care App", version="1.0.0")

@app.on_event("startup")
async def startup():
    # 데이터베이스 테이블 생성 (초기 개발 단계에 유용)
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    pass

# API 라우터 포함
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}