import cv2
from ultralytics import YOLO
import asyncio
import edge_tts
import pygame
import time
import os

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(0)

pygame.mixer.init()

last_spoken = 0
cooldown = 3


async def speak(text):

    filename = "speech.mp3"

    communicate = edge_tts.Communicate(text, "en-IN-NeerjaNeural")
    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()   # important
    pygame.mixer.music.unload() # important

    os.remove(filename)


while True:

    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.5)

    detected = []

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])
            name = model.names[cls]

            detected.append(name)

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,255), 3)
            cv2.putText(frame, name, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255), 2)

    now = time.time()

    if detected and now - last_spoken > cooldown:

        text = "I see " + ", ".join(set(detected))
        print(text)

        asyncio.run(speak(text))

        last_spoken = now

    cv2.imshow("AI Vision Assistant", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()