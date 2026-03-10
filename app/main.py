import cv2
import numpy as np
import asyncio
import os

from detection import detect_objects
from face_detection import detect_face
from hand_raise import detect_hand_raise
from behavior import analyze
from speech import speak
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
last_behavior = None

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze")
async def analyze_frame(file: UploadFile = File(...)):

    global last_behavior

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)

    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    objects = detect_objects(frame)

    face_detected = detect_face(frame)

    hand_raised = detect_hand_raise(frame)

    behavior = analyze(objects, face_detected, hand_raised)

    if behavior != last_behavior:
        await speak(behavior)
        last_behavior = behavior

    return {
        "objects": objects,
        "behavior": behavior
    }