# emotion_detector.py
import cv2
from fer import FER

def detect_emotion_from_frame(frame, detector):
    result = detector.top_emotion(frame)
    if result:
        emotion, score = result
        return emotion
    return "neutral"

def start_camera():
    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(0)
    return cap, detector
