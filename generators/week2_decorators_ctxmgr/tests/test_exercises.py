import os
import time

from generators.week2_decorators_ctxmgr.exercises import timing, retry, temporary_file


def test_timing_print(capsys):
    @timing()
    def f():
        time.sleep(0.01)

    f()
    captured = capsys.readouterr()
    assert "f took" in captured.out


def test_retry_success_after_fail():
    calls = {"n": 0}

    @retry(times=3, delay=0)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 2:
            raise ValueError("fail")
        return "ok"

    assert flaky() == "ok"


def test_temporary_file(tmp_path):
    p = tmp_path / "should_not_exist.txt"
    with temporary_file("hello") as path:
        assert os.path.exists(path)
        with open(path, "r", encoding="utf-8") as f:
            assert f.read() == "hello"
    assert not os.path.exists(path)
