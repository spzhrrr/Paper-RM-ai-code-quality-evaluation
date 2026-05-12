def binary_search(arr: list, target: int) -> int:
    """Search for target in a sorted list using binary search.

    Uses Knuth's midpoint formula (left + (right-left)//2) to avoid
    integer overflow in languages with fixed-width integers.
    Time complexity: O(log n).  Space complexity: O(1).

    Args:
        arr: A sorted list of comparable elements.
        target: The element to search for.

    Returns:
        The index of target in arr, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
