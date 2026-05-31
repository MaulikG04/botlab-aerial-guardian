from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Run tracking on only first few frames
results = model.track(
    source="/Users/maulikgautam/Desktop/VisDrone2019-MOT-val/sequences/uav0000086_00000_v",
    tracker="bytetrack.yaml",
    persist=True,
    stream=True
)

# Inspect first 3 frames only
for frame_idx, result in enumerate(results):

    print(f"\n{'='*50}")
    print(f"FRAME {frame_idx}")
    print(f"{'='*50}")

    if result.boxes is None:
        print("No detections")
        continue

    for box in result.boxes:

        track_id = None
        if box.id is not None:
            track_id = int(box.id.item())

        cls_id = int(box.cls.item())
        confidence = float(box.conf.item())

        x_center, y_center, width, height = box.xywh[0].tolist()

        print(
            f"ID={track_id}, "
            f"CLASS={cls_id}, "
            f"CONF={confidence:.3f}, "
            f"XYWH=({x_center:.1f}, {y_center:.1f}, {width:.1f}, {height:.1f})"
        )

    # Stop after first 3 frames
    if frame_idx >= 2:
        break