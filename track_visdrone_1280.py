from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="/Users/maulikgautam/Desktop/VisDrone2019-MOT-val/sequences/uav0000086_00000_v",
    tracker="bytetrack.yaml",
    persist=True,
    save=True,
    imgsz=1280
)

print("Done")