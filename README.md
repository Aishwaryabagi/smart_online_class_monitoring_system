Smart Classroom Monitoring System

An AI-powered system that monitors student engagement during online classes using Computer Vision and Speech Feedback. The system analyzes webcam frames in real time to detect behaviors such as phone usage, attention level, hand raising, and absence from the camera.

The application uses YOLO object detection, OpenCV-based analysis, and FastAPI to provide real-time behavioral feedback and voice alerts.

Features

Real-time classroom monitoring

Detects student using phone

Detects student looking away from camera

Detects raised hand gesture

Detects student absence from camera

Provides voice feedback using text-to-speech

Interactive Start / End classroom dashboard

FastAPI backend with REST API

Docker containerization for easy deployment

System Architecture
Browser Camera
       │
       ▼
HTML Dashboard (Start / End Class)
       │
       ▼
FastAPI Server
       │
       ▼
Computer Vision Pipeline
       │
       ├── YOLO Object Detection
       ├── Face Detection
       ├── Motion Detection
       ▼
Behavior Analysis Engine
       │
       ▼
Speech Output + API Response
Detected Behaviors
Behavior	Detection Logic
Student using phone	YOLO detects person and cell phone
Student looking away	Face detection fails
Student raised hand	Motion detection across frames
Student attentive	Person detected and face visible
Student not active	No person detected
Technology Stack
Backend

FastAPI

Python

Computer Vision

OpenCV

YOLO (Ultralytics)

Frontend

HTML

JavaScript

Jinja2 Templates

Speech

Edge TTS

Pygame

Deployment

Docker

Uvicorn

Project Structure
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
├── requirements.txt
├── Dockerfile
└── README.md
Installation (Local Setup)
Clone the repository
git clone https://github.com/your-username/smart-online-class-monitoring.git
cd smart-online-class-monitoring
Create virtual environment
python -m venv .venv

Activate environment

Windows

.venv\Scripts\activate

Mac/Linux

source .venv/bin/activate
Install dependencies
pip install -r requirements.txt
Run the server
uvicorn app.main:app --reload

Open in browser

http://127.0.0.1:8000

API documentation

http://127.0.0.1:8000/docs
Running with Docker
Build the Docker image
docker build -t smart-classroom-ai .
Run the container
docker run -p 8000:8000 smart-classroom-ai

Access the application

http://localhost:8000
API Endpoint
Analyze Frame
POST /analyze

Input

Image frame

Response

{
  "objects": ["person"],
  "behavior": "Student attentive"
}
Future Improvements

Pose estimation for accurate hand raise detection

Head pose estimation for better attention tracking

Multi-student monitoring

Real-time bounding box visualization

WebSocket streaming for lower latency

Use Cases

Online classrooms

Student engagement analytics

AI-assisted teaching systems

Remote learning monitoring

Author

Developed by Aishwarya Bagi

AI / Machine Learning Enthusiast
Interested in Computer Vision and AI Systems
