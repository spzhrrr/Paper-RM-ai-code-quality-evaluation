def merge_sort(arr: list) -> list:
    """Return a new sorted list produced by the merge sort algorithm.

    The input list is not mutated.

    Time complexity : O(n log n) — best, average, and worst cases.
    Space complexity: O(n) — new sub-lists are allocated during merging.

    Args:
        arr: A list of comparable elements.

    Returns:
        A new list containing the same elements in ascending order.
    """
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])
    return _merge(left_sorted, right_sorted)


def _merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
