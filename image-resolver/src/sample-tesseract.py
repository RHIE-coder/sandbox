from PIL import Image
import pytesseract
from pathlib import Path


img_name = "image.png"
input_path = Path(".").joinpath("assets",img_name)

def extract_text_from_image(image_path, box=None):
    """
    이미지를 불러와서 지정된 영역에서 텍스트를 추출합니다.
    
    Parameters:
    - image_path (str): 이미지 파일 경로
    - box (tuple): 잘라낼 영역의 좌표 (left, upper, right, lower), 지정하지 않으면 전체 이미지 사용
    
    Returns:
    - str: 추출된 텍스트
    """
    # 이미지 열기
    with Image.open(image_path) as img:
        # 특정 영역 잘라내기 (box가 지정된 경우)
        if box:
            img = img.crop(box)
        
        # OCR을 사용하여 텍스트 추출
        text = pytesseract.image_to_string(img, lang='eng+kor')
        return text

# 예시: 이미지에서 텍스트 추출
# box_coordinates = (100, 100, 400, 400)  # 필요한 경우, 영역 지정 (없으면 None으로)
# extracted_text = extract_text_from_image(input_path, box_coordinates)
extracted_text = extract_text_from_image(input_path)

print("Extracted Text:")
print(extracted_text)