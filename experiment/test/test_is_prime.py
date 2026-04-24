import pytest

def test_less_than_two():
    from solution import is_prime
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-3) is False

def test_primes():
    from solution import is_prime
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(13) is True

def test_composites():
    from solution import is_prime
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(100) is False
