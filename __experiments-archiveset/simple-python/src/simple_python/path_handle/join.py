from pathlib import Path
print(__file__)

p = Path(__file__).resolve()


with open(p, 'rb') as f:
    content = f.read().decode('utf-8')

    output_file_path = Path("output.py")

    # 내용을 새로운 파일에 저장
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(content)