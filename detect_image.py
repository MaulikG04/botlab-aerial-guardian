from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="input/test.jpg",
    save=True
)

print("Detection complete!")