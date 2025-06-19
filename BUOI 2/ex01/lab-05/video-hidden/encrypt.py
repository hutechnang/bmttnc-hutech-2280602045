import sys
import os
import cv2
import numpy as np
from PIL import Image
from cryptography.fernet import Fernet

def encrypt_message(message, key_path):
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

def encode_message_to_frame(frame, message_bytes):
    binary_data = ''.join([format(byte, '08b') for byte in message_bytes]) + '11111110'
    h, w, _ = frame.shape
    total_pixels = h * w * 3
    if len(binary_data) > total_pixels:
        raise ValueError("Dữ liệu quá lớn để nhúng vào video")

    flat_frame = frame.flatten()
    for i in range(len(binary_data)):
        # Đảm bảo giá trị nằm trong phạm vi uint8 (0-255)
        current_value = flat_frame[i]
        new_value = (current_value & 0xFE) | int(binary_data[i])  # 0xFE = 254, giữ 7 bit cao, thay LSB
        flat_frame[i] = new_value

    return flat_frame.reshape(frame.shape)

def encrypt_video(video_path, message, output_path, key_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Không tìm thấy video: {video_path}")

    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = None

    encrypted_bytes = encrypt_message(message, key_path)
    message_embedded = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if not out:
            h, w = frame.shape[:2]
            out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (w, h))

        if not message_embedded:
            frame = encode_message_to_frame(frame, encrypted_bytes)
            message_embedded = True

        out.write(frame)

    cap.release()
    out.release()

def main():
    if len(sys.argv) != 3:
        print("Cách dùng: python encrypt.py <video_path> <message>")
        return
    video_path = sys.argv[1]
    message = sys.argv[2]
    output_path = "encoded_video.avi"
    key_path = "secret.key"
    encrypt_video(video_path, message, output_path, key_path)
    print("Mã hóa hoàn tất.")
    print("Video nhúng: ", output_path)
    print("Key lưu tại: ", key_path)

if __name__ == "__main__":
    main()
