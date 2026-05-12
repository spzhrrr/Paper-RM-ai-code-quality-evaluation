import csv
from collections import defaultdict


def aggregate_csv(filepath: str) -> dict:
    """Parse a CSV file and return the summed value per group.

    The CSV must have a header row with columns 'group' and 'value'.
    Each group's values are summed and rounded to 2 decimal places.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A dict mapping group name (str) to aggregated value (float).

    Time complexity: O(n) where n is the number of rows.
    Space complexity: O(g) where g is the number of unique groups.
    """
    totals: dict = defaultdict(float)
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            totals[row['group']] += float(row['value'])
    return {group: round(total, 2) for group, total in totals.items()}
