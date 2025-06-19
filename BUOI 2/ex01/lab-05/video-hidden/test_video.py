import cv2

cap = cv2.VideoCapture("encoded_video.avi")
if not cap.isOpened():
    print("Không thể mở video!")
else:
    ret, frame = cap.read()
    if ret:
        print("Đọc frame thành công, kích thước:", frame.shape)
    else:
        print("Không thể đọc frame!")
cap.release()