import os
os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"  # Pour éviter certains bugs

import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
CONFIDENCE_THRESHOLD = 0.5
TARGET_CLASSES = ["car", "person", "dog"]
DEVICE = "cpu"  # "cuda" si GPU

model = YOLO("yolov8m.pt")

st.title("🎯 Détection d’objets sur une vidéo avec YOLOv8")
st.markdown("Téléversez une vidéo pour lancer la détection d’objets (car, person, dog).")

video_file = st.file_uploader("📤 Upload votre vidéo", type=["mp4", "avi", "mov"])

if video_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    if st.button("Lancer la détection"):
        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        frame_count = 0
        MAX_FRAMES = 100  # Limite pour éviter blocage navigateur

        while cap.isOpened() and frame_count < MAX_FRAMES:
            ret, frame = cap.read()
            if not ret:
                break

            result = model(frame, device=DEVICE)[0]
            boxes = result.boxes.xyxy.cpu().numpy().astype(int)
            classes = result.boxes.cls.cpu().numpy().astype(int)
            confs = result.boxes.conf.cpu().numpy()

            for cls, box, conf in zip(classes, boxes, confs):
                if conf < CONFIDENCE_THRESHOLD:
                    continue

                label = model.names[cls]
                if TARGET_CLASSES and label not in TARGET_CLASSES:
                    continue

                x1, y1, x2, y2 = box
                color = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label}: {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame_rgb, channels="RGB")
            frame_count += 1

        cap.release()
        st.success("Détection terminée.")
