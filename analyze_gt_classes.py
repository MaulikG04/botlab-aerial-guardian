from collections import Counter

GT_FILE = "/Users/maulikgautam/Desktop/VisDrone2019-MOT-val/annotations/uav0000086_00000_v.txt"

class_counter = Counter()

with open(GT_FILE, "r") as f:
    for line in f:
        parts = line.strip().split(",")

        # VisDrone class field
        class_id = int(parts[7])

        class_counter[class_id] += 1

print("\nGround Truth Class Distribution\n")

for cls, count in sorted(class_counter.items()):
    print(f"Class {cls}: {count}")