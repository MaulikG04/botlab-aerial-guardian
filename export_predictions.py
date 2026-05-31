from ultralytics import YOLO
from pathlib import Path

# -------------------------------
# CONFIG
# -------------------------------

SEQUENCE_PATH = "/Users/maulikgautam/Desktop/VisDrone2019-MOT-val/sequences/uav0000086_00000_v"

OUTPUT_FILE = "predictions.txt"

# -------------------------------
# LOAD MODEL
# -------------------------------

model = YOLO("yolov8n.pt")

# -------------------------------
# TRACK
# -------------------------------

results = model.track(
    source=SEQUENCE_PATH,
    tracker="bytetrack.yaml",
    persist=True,
    stream=True,
    imgsz=1280
)

# -------------------------------
# EXPORT
# -------------------------------

with open(OUTPUT_FILE, "w") as f:

    for frame_idx, result in enumerate(results, start=1):

        if result.boxes is None:
            continue

        for box in result.boxes:

            # Skip non-person classes
            cls_id = int(box.cls.item())

            if cls_id != 0:
                continue

            track_id = -1

            if box.id is not None:
                track_id = int(box.id.item())

            confidence = float(box.conf.item())

            x_center, y_center, width, height = box.xywh[0].tolist()

            # Convert center format -> top-left format
            left = x_center - width / 2
            top = y_center - height / 2

            line = (
                f"{frame_idx},"
                f"{track_id},"
                f"{left:.2f},"
                f"{top:.2f},"
                f"{width:.2f},"
                f"{height:.2f},"
                f"{confidence:.4f},"
                f"{cls_id}\n"
            )

            f.write(line)

print(f"Predictions saved to {OUTPUT_FILE}")