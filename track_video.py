from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="input/test_video.mp4",
    tracker="bytetrack.yaml",
    persist=True,
    save=True
)

print("Tracking complete!")