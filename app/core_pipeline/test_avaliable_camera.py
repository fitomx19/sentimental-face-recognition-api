import cv2

def test_camera(index):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Cámara {index}: Disponible")
        cap.release()
    else:
        print(f"Cámara {index}: No disponible")

def check_available_cameras():
    for index in range(10):  # Intentar hasta el índice 9
        test_camera(index)

check_available_cameras()
