import pytest

from generators.week1_generators.exercises import (
    chunked,
    sliding_window,
    read_lines,
    words_from_iter,
    pipeline_filter_map,
)


def test_chunked():
    assert list(chunked([1,2,3,4,5],2)) == [[1,2],[3,4],[5]]


def test_sliding():
    assert list(sliding_window([1,2,3,4],2)) == [(1,2),(2,3),(3,4)]


def test_pipeline_filter_map(tmp_path):
    p = tmp_path / "s.txt"
    p.write_text("a\nB\nc\n")
    lines = list(read_lines(str(p)))
    res = list(pipeline_filter_map(lines, lambda s: s.islower(), lambda s: s.upper()))
    assert res == ["A","C"]


def test_words_from_iter():
    lines = ["one two","three"]
    assert list(words_from_iter(lines)) == ["one","two","three"]
