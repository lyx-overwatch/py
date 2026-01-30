from generators.week4_types_testing.exercises import add_numbers, concat_strings


def test_add_numbers():
    assert add_numbers(1, 2) == 3


def test_concat_strings():
    assert concat_strings(["a", "b"]) == "ab"
