from ultralytics import YOLO

model = YOLO("models/yolo11n.pt")

def detect_objects(frame):

    results = model(frame, conf=0.5)

    detected = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            name = model.names[cls]
            detected.append(name)

    return list(set(detected))