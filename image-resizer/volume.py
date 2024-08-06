from PIL import Image

target_name = 'imghigh.jpg'
size = 1600 

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        resized_img = img.resize(size)
        resized_img.save(output_path, quality=100)
        print(f"이미지 크기 조절 완료: {output_path}")

input_image_path = f'./images/source/{target_name}'
output_image_path = f'./images/destination/{size}x{size}-2.jpg'
new_size=(size, size)

resize_image(input_image_path, output_image_path, new_size)