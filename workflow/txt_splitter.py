with open("data/word_lists_primary_only.txt", "r") as f:
    content = f.read().strip()

groups = content.split("\n\n")

rows = [group.split("\n") for group in groups]

import csv
with open("data/adjusted_word_lists_primary_only.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)