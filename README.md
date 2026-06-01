# The Aerial Guardian

Drone-based human detection and tracking system developed for the BotLab Dynamics Research Engineer (Computer Vision & Deep Learning) assignment.

## Objective

Detect and track people from aerial drone footage while maintaining stable identities across frames.

## Dataset

VisDrone2019-MOT Validation Dataset

## Pipeline

VisDrone Frames

↓

YOLOv8 (Human Detection)

↓

ByteTrack (Multi-Object Tracking)

↓

Evaluation Framework

↓

Failure Analysis & Optimization

## Experiments

### Baseline

* YOLOv8n
* ByteTrack
* Resolution: 640

### Optimized

* YOLOv8n
* ByteTrack
* Resolution: 1280

## Key Findings

A custom discrepancy analysis framework was developed to compare predictions against VisDrone ground-truth annotations.

On a difficult benchmark frame:

* Ground Truth: 69 humans
* YOLOv8n @ 640: 18 detections
* YOLOv8n @ 1280: 39 detections

Increasing inference resolution significantly improved small-object detection performance.

Remaining failures were primarily associated with:

* Extremely small distant humans
* Heavy occlusions
* Seated individuals

## Repository Structure

* track_visdrone.py – baseline tracking
* track_visdrone_1280.py – optimized tracking
* export_predictions.py – prediction export
* frame_discrepancy_report.py – evaluation framework
* analyze_gt_classes.py – dataset analysis

## Future Work

* Trajectory visualization
* Camera motion compensation
* YOLOv8s benchmarking
* Occlusion-aware tracking improvements
