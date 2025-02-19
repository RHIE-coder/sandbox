from sqlalchemy_schemadisplay import create_uml_graph
from sqlalchemy.orm import class_mapper
from myapp.models import Base  # SQLAlchemy 모델의 Base 가져오기

# 모델에서 UML 그래프 생성
graph = create_uml_graph(
    Base.metadata,  # SQLAlchemy의 메타데이터 전달
    show_operations=False,  # 함수(메서드) 표시 X
    show_multiplicity_one=False  # 1:1 관계 표시 X
)

# 이미지 파일로 저장 (PNG 형식)
graph.write_png("schema.png")
