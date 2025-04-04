from sqlalchemy_schemadisplay import create_uml_graph
from sqlalchemy.orm import class_mapper
from sqlmodel import SQLModel
from models import User, Post  # SQLModel에서 모델을 가져옴

# SQLModel의 테이블들을 ERD에 반영하기 위해 Mapper 추출
mappers = [class_mapper(model) for model in [User, Post]]

# ERD 생성
graph = create_uml_graph(
    mappers,
    show_operations=False,
    show_multiplicity_one=False
)

# 이미지 저장
graph.write_png("schema.png")
print("✅ ERD가 'schema.png'로 저장되었습니다.")
