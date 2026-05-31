GT_FILE = "/Users/maulikgautam/Desktop/VisDrone2019-MOT-val/annotations/uav0000086_00000_v.txt"

seen = set()

with open(GT_FILE) as f:
    for line in f:

        parts = line.strip().split(",")

        cls = int(parts[7])

        if cls not in seen:
            print(line.strip())
            seen.add(cls)

        if len(seen) == 5:
            break