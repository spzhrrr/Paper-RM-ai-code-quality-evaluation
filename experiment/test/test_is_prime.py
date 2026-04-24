import pytest
# Import target function — replace source module per model under test
from solution import is_prime

def test_less_than_two_returns_false():
    """n < 2 must return False (edge case: boundary handling)."""
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False

def test_known_primes():
    """Standard prime numbers must return True."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(13) is True
    assert is_prime(97) is True

def test_known_composites():
    """Composite numbers must return False."""
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(100) is False

def test_even_prime():
    """2 is the only even prime; must not be filtered by even-number shortcut."""
    assert is_prime(2) is True

def test_large_prime():
    """Large prime must return True within reasonable time."""
    assert is_prime(7919) is True
