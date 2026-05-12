import csv


def aggregate_csv(filepath):
    result = {}
    with open(filepath, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            group = row['group']
            value = float(row['value'])
            result[group] = result.get(group, 0) + value
    return {k: round(v, 2) for k, v in result.items()}
