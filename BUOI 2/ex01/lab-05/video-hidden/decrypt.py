import sys
import os
import cv2
from PIL import Image
from cryptography.fernet import Fernet

def extract_message_from_frame(frame):
    binary_data = ""
    stop = False
    h, w, _ = frame.shape

    for row in range(h):
        for col in range(w):
            for ch in range(3):  # BGR
                lsb = frame[row, col][ch] & 1
                binary_data += str(lsb)
                if binary_data.endswith("11111110"):
                    stop = True
                    break
            if stop: break
        if stop: break

    end = binary_data.find("11111110")
    if end == -1:
        raise ValueError("Không tìm thấy dấu kết thúc")

    binary_data = binary_data[:end]

    while len(binary_data) % 8 != 0:
        binary_data = binary_data[:-1]

    return bytes([int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)])

def decrypt_video(video_path, key_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Không tìm thấy video: {video_path}")
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Không tìm thấy key: {key_path}")

    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise ValueError("Không đọc được frame đầu tiên.")

    data_bytes = extract_message_from_frame(frame)

    with open(key_path, "rb") as f:
        key = f.read()

    cipher = Fernet(key)
    decrypted = cipher.decrypt(data_bytes).decode()
    return decrypted

def main():
    if len(sys.argv) != 2:
        print("Cách dùng: python decrypt.py <encoded_video_path>")
        return

    video_path = sys.argv[1]
    message = decrypt_video(video_path, "secret.key")
    print("✅ Giải mã thành công!")
    print("🔓 Tin nhắn:", message)

if __name__ == "__main__":
    main()
