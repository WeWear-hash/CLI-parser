import csv

def count_rows(file_path):
    with open(file_path, "r") as f:
        content = csv.DictReader(f)
        rows = [row for row in content]
        return len(rows)