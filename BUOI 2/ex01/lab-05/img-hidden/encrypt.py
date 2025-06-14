import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '11111110'  # Thêm ký hiệu kết thúc
    if len(binary_message) > width * height * 3:
        raise ValueError("Message too long to encode in this image!")

    index = 0
    encoded_img = img.copy()
    pixels = encoded_img.load()

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                pixel = list(pixels[col, row])
                for i in range(3):  # RGB
                    if index < len(binary_message):
                        # Thay đổi bit cuối cùng của mỗi kênh màu
                        binary_value = format(pixel[i], '08b')
                        binary_value = binary_value[:-1] + binary_message[index]
                        pixel[i] = int(binary_value, 2)
                        index += 1
                pixels[col, row] = tuple(pixel)

    encoded_img.save("encoded_image.png")
    print("Steganography complete. Encoded image saved as encoded_image.png")

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    image_path, message = sys.argv[1], sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()