from ultralytics import YOLO
import torch

print("Torch:", torch.__version__)
print("MPS Available:", torch.backends.mps.is_available())

model = YOLO("yolov8n.pt")

print("Model loaded successfully")