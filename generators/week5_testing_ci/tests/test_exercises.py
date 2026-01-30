import pytest

from generators.week5_testing_ci.exercises import is_prime


@pytest.mark.parametrize("n,expected", [(1, False), (2, True), (17, True), (18, False)])
def test_is_prime(n, expected):
    assert is_prime(n) == expected
