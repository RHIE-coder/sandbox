from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "sqlite:///database.db"

# SQLite 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)

# 데이터베이스 세션 생성
def get_session():
    with Session(engine) as session:
        yield session
