from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

# 데이터베이스 설정 및 ORM 기본 클래스 생성
DATABASE_URL = "sqlite:///local.db"  # SQLite3 파일 DB
engine = create_engine(DATABASE_URL, echo=True)  # echo=True: 쿼리 로그 출력
Session = sessionmaker(bind=engine)  # 세션 생성

class Base(DeclarativeBase):
    pass

# User 테이블 정의
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# 데이터베이스 및 테이블 생성
Base.metadata.create_all(engine)

# # 데이터 추가 및 업데이트
# def main():
#     session = Session()
#     try:
#         # 1. 데이터 추가
#         new_user = User(name="Alice", age=25)
#         session.add(new_user)
#         session.commit()
#         print("User 추가 완료.")

#         # 2. 데이터 조회
#         user = session.query(User).filter_by(name="Alice").first()
#         print(f"조회된 User: ID={user.id}, Name={user.name}, Age={user.age}")

#         # 3. 데이터 업데이트
#         user.age = 30
#         session.commit()
#         print("User 업데이트 완료.")

#         # 4. 업데이트 후 확인
#         updated_user = session.query(User).filter_by(name="Alice").first()
#         print(f"업데이트된 User: ID={updated_user.id}, Name={updated_user.name}, Age={updated_user.age}")
#     except Exception as e:
#         session.rollback()
#         print(f"오류 발생: {e}")
#     finally:
#         session.close()

# if __name__ == "__main__":
#     main()