from .demo import run
from .demo import OUTFILE

EXPECTED="""11,ten_identical_values
1001,more_than_0.7
1011,ten_identical_values
2011,ten_identical_values
"""
def test_e2e_demo():
    assert OUTFILE.read_text() == EXPECTED
