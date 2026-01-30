from generators.week6_concurrency_parallel.exercises import run_thread_pool, run_process_pool


def test_run_thread_pool():
    res = run_thread_pool(list(range(10)), workers=3)
    assert res == list(range(10))


def test_run_process_pool():
    res = run_process_pool([5,6], workers=2)
    assert res == [5,8]
