from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("input/test.jpg")

result = results[0]

for box in result.boxes:
    print("Class:", int(box.cls))
    print("Confidence:", float(box.conf))
    print("Coordinates:", box.xyxy.tolist())
    print("-" * 30)