# Gesture-Controlled-Robotic-Arm
A simple robotic arm simulation using hand gestures via Mediapipe + OpenCV.
A Python-Based simulated robotic arm that responds to hand gestures using OpenCV and Mediapipe. Designed for real-time control
and educational purposes.

# 🤖 Gesture-Controlled Robotic Arm (Python + Mediapipe)
This project simulates a robotic arm controlled by hand gestures using your webcam. Built with Python, OpenCV, and Mediapipe.

## 🔧 Features
- Real-time hand tracking using webcam
- Detects number of fingers to control robot actions
- Simulates robotic arm commands like:
  - Move Left / Right / Up / Down
  - Grab Object
  - 
## 🖥 Technologies Used
- Python 3.10
- OpenCV
- Mediapipe
- NumPy

## 📦 Installation
1. Clone this repo or download files
2. Create a virtual environment (optional but recommended)
3. Install dependencies:

```bash
pip install -r requirements.txt

🖐 Gesture Mapping
Fingers Shown	Action
0	Arm is Idle
1	Move Right
2	Move Left
3	Move Up
4	Move Down
5	Grab Object

## How it works
- The webcam captures real-time hand movements.
- MediaPipe processes hand landmarks.
- Gestures are mapped to robotic arm movements.
- OpenCV simulates the arm response on screen

📚 Learnings
As a beginner, this was a great project to understand:
How computer vision and hand tracking work
Basic inverse kinematics
Simulating a robot using just Python and OpenCV
Working with external libraries and managing dependencies

##  📸Demo
![Project Demo](screenshot.png)


## 🪪 License
[MIT License](LICENSE)
This project is licensed under the MIT License
