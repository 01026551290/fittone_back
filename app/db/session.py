from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 비동기 엔진 생성
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# 비동기 세션 팩토리 생성
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 종속성으로 사용할 데이터베이스 세션 생성 함수
from typing import AsyncGenerator

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session