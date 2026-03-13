# 🎓 Smart Classroom Monitoring System

An AI-powered **Smart Classroom Monitoring System** that analyzes student engagement during online classes using **Computer Vision and FastAPI**.

The system processes webcam frames in real time to detect behaviors such as **phone usage, attention level, raised hand gestures, and absence from the camera**, helping teachers monitor student engagement during virtual classes.

---

## 🚀 Demo

![Demo](demo.gif)

The system provides a **browser dashboard with Start / End Classroom controls** and performs **real-time behavior analysis using a computer vision pipeline**.

---

## ✨ Features

* Real-time classroom monitoring
* Detects **student using phone**
* Detects **student looking away from camera**
* Detects **raised hand gesture**
* Detects **student absence from camera**
* Provides **voice alerts using Text-to-Speech**
* Browser dashboard with **Start / End Classroom**
* FastAPI backend with REST API

---

## 🧠 System Architecture

```
Browser Webcam
      │
      ▼
HTML Dashboard (Start / End Classroom)
      │
      ▼
FastAPI Backend
      │
      ▼
Computer Vision Pipeline
      │
      ├── YOLO Object Detection
      ├── Face Detection (OpenCV)
      ├── Motion Detection
      ▼
Behavior Analysis Engine
      │
      ▼
Voice Feedback + API Response
```

---

## 📌 Detected Behaviors

| Behavior             | Detection Logic                        |
| -------------------- | -------------------------------------- |
| Student using phone  | YOLO detects `person` and `cell phone` |
| Student looking away | Face detection fails                   |
| Student raised hand  | Motion detection across frames         |
| Student attentive    | Person detected and face visible       |
| Student not active   | No person detected                     |

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Computer Vision

* OpenCV
* YOLO (Ultralytics)

### Frontend

* HTML
* JavaScript
* Jinja2 Templates

### Speech

* Edge-TTS
* Pygame

---

## 📂 Project Structure

```
smart-online-class-monitoring
│
├── app
│   ├── main.py
│   ├── detection.py
│   ├── face_detection.py
│   ├── hand_raise.py
│   ├── behavior.py
│   ├── speech.py
│   ├── templates
│   │    └── index.html
│   └── models
│        └── yolo11n.pt
│
├── demo.gif
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/your-username/smart-online-class-monitoring.git
cd smart-online-class-monitoring
```

Create virtual environment

```
python -m venv .venv
```

Activate environment

Windows

```
.venv\Scripts\activate
```

Mac / Linux

```
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server

```
uvicorn app.main:app --reload
```

Open browser

```
http://127.0.0.1:8000
```

API documentation

```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoint

### Analyze Frame

```
POST /analyze
```

Input

* Webcam frame from browser

Example Response

```json
{
  "objects": ["person"],
  "behavior": "Student attentive"
}
```

---

## 🔮 Future Improvements

* Pose estimation for accurate hand-raise detection
* Head pose estimation for attention tracking
* Multi-student monitoring
* Real-time bounding boxes on video stream
* Docker containerization and cloud deployment

---

## 👩‍💻 Author

**Aishwarya Bagi**

AI / Machine Learning Enthusiast
Interested in Computer Vision and AI Systems
