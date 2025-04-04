import sys
import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from sqlmodel import SQLModel
from models import User, Post  # SQLModel을 사용한 테이블을 정의한 파일

# Alembic 설정 가져오기
config = context.config

# 데이터베이스 연결 정보
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=SQLModel.metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=SQLModel.metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
