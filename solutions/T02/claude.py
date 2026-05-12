def reverse_string(s: str) -> str:
    """Reverse a string using an in-place two-pointer swap on a char list.

    Does not use slicing [::-1] or the built-in reversed() function.
    Time complexity: O(n).  Space complexity: O(n).
    """
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)
