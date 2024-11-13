import easyocr
from pathlib import Path


img_name = "image.png"
input_path = str(Path(".").joinpath("assets",img_name))

reader = easyocr.Reader(['en', 'ko'])  # 영어와 한국어 언어 모델 로딩
result = reader.readtext(input_path)

for detection in result:
    text = detection[1]  # 텍스트 부분
    confidence = detection[2]  # 신뢰도
    # print(f"Detected text: {text}, Confidence: {confidence:.2f}")
    print(text)