# alembic/env.py

import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context
import os
import sys
from dotenv import load_dotenv

# 프로젝트 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# .env 파일 로드
load_dotenv()

from app.db.base import Base
from app.core.config import settings

# Alembic 설정 읽기
config = context.config

# 데이터베이스 URL 설정
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# 로깅 설정
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 메타데이터 가져오기
target_metadata = Base.metadata

def run_migrations_offline():
    """오프라인 모드에서 마이그레이션을 실행합니다."""
    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    """온라인 모드에서 마이그레이션을 실행합니다."""
    connectable = create_async_engine(
        settings.DATABASE_URL,
        poolclass=pool.NullPool,
        echo=True
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())