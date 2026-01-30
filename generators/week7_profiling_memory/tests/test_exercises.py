from generators.week7_profiling_memory.exercises import expensive_calc


def test_expensive_calc():
    assert isinstance(expensive_calc(10), int)
