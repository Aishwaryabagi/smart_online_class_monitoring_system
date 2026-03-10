import cv2
import numpy as np

previous_frame = None

def detect_hand_raise(frame):

    global previous_frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if previous_frame is None:
        previous_frame = gray
        return False

    diff = cv2.absdiff(previous_frame, gray)

    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    motion_pixels = np.sum(thresh > 0)

    previous_frame = gray

    if motion_pixels > 15000:
        return True

    return False