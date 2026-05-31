from collections import defaultdict

# ---------------------------------
# FILES
# ---------------------------------

GT_FILE = "/Users/maulikgautam/Desktop/VisDrone2019-MOT-val/annotations/uav0000086_00000_v.txt"
PRED_FILE = "predictions.txt"

# ---------------------------------
# COUNT HUMAN GT OBJECTS PER FRAME
# ---------------------------------

gt_counts = defaultdict(int)

with open(GT_FILE, "r") as f:
    for line in f:

        parts = line.strip().split(",")

        frame_id = int(parts[0])

        category = int(parts[7])

        # VisDrone human categories
        if category not in [1, 2]:
            continue

        gt_counts[frame_id] += 1
# ---------------------------------
# COUNT PRED OBJECTS PER FRAME
# ---------------------------------

pred_counts = defaultdict(int)

with open(PRED_FILE, "r") as f:
    for line in f:

        parts = line.strip().split(",")

        frame_id = int(parts[0])

        pred_counts[frame_id] += 1

# ---------------------------------
# COMPARE
# ---------------------------------

all_frames = sorted(
    set(gt_counts.keys()) |
    set(pred_counts.keys())
)

report = []

for frame in all_frames:

    gt = gt_counts.get(frame, 0)
    pred = pred_counts.get(frame, 0)

    diff = abs(gt - pred)

    report.append(
        (diff, frame, gt, pred)
    )

# ---------------------------------
# SORT WORST FIRST
# ---------------------------------

report.sort(reverse=True)

print("\nTop 20 Most Suspicious Frames\n")
print(
    f"{'Frame':<10}"
    f"{'GT':<10}"
    f"{'Pred':<10}"
    f"{'Diff':<10}"
)

print("-" * 40)

for diff, frame, gt, pred in report[:20]:

    print(
        f"{frame:<10}"
        f"{gt:<10}"
        f"{pred:<10}"
        f"{diff:<10}"
    )