# YOLOv8 Video Object Detection – Streamlit App

This project is a Proof of Concept (POC) for real-time object detection in videos using **YOLOv8** and **OpenCV**, wrapped in an interactive **Streamlit** web application. It allows users to upload a video and see object detection in action (e.g., car, person, dog).

> The code is compatible with both CPU and GPU. If using GPU (CUDA), set the `DEVICE` variable accordingly in `app.py`.

---

## 📽️ Video Presentation

A video presentation that goes through the environment setup, code explanation, and demo. The video does not exceed 7 minutes:  
👉 [Watch the presentation here](https://drive.google.com/file/d/1V4_DVw1Pie0U7_zk-SFJ-GZM7qSYlvay/view?usp=drive_link)

---

## 📁 Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Video Demo](#video-presentation)  
- [Contributing](#contributing)  
- [License](#license)

---

## 🚀 Features

- Web-based user interface via **Streamlit**
- Upload and process video files (`.mp4`, `.avi`, `.mov`)
- Real-time object detection using **YOLOv8m**
- Detection limited to selected target classes: `car`, `person`, `dog`
- Runs on **CPU or GPU**
- Displays bounding boxes with confidence scores

---

## 🛠️ Installation

To install and run the project locally:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/jansonz/yolov8-video-object-detection
   cd yolov8-video-object-detection
