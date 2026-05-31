from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="input/test_video.mp4",
    save=True
)

print("Video processing complete!")