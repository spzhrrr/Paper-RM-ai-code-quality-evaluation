def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise.

    Uses trial division up to sqrt(n) with 2- and 3-wheel optimisation.
    Time complexity: O(sqrt(n)).  Space complexity: O(1).
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    if n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
