import pytest

from .demo import gen_run_length
from .demo import gen_rising_edge


@pytest.mark.parametrize("test_input,expected", [
    ([], []),
    ([0], [0]),
    ([0, 0], [0, 1]),
    ([0, 0, 0, 1, 1, 1, 1, 2, 2], [0, 1, 2, 0, 1, 2, 3, 0 ,1])
])
def test_gen_run_length(test_input, expected):
    assert list(gen_run_length(test_input)) == expected


@pytest.mark.parametrize("test_input,threshold,expected", [
    ([], 1, []),
    ([0], 1, [False]),
    ([0, 0], 1, [False, False]),
    ([0, 0, 0, 1, 1, 1, 1, 2, 2], 1, [False]*7 + [True, False]),  # detects a rising edge
    (reversed([0, 0, 0, 1, 1, 1, 1, 2, 2]), 1, [False]*9)  # does not detect a falling edge
])
def test_gen_rising_edge(test_input, threshold, expected):
    assert list(gen_rising_edge(test_input, threshold)) == expected

