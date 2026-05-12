import csv


def aggregate_csv(filepath):
    aggregated = {}
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row['group']
            val = float(row['value'])
            if key in aggregated:
                aggregated[key] += val
            else:
                aggregated[key] = val
    return {k: round(v, 2) for k, v in aggregated.items()}
