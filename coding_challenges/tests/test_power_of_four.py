
# -*- coding: utf-8 -*-
"""
Pytest file for the Power of Four coding challenge.
"""
import pytest
from solutions.solution_150 import isPowerOfFour


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (4, True),
        (16, True),
        (64, True),
        (256, True),
        (1024, True),
        (4096, True),
        (16384, True),
        (65536, True),
        (262144, True),
        (1048576, True),
        (0, False),
        (2, False),
        (3, False),
        (5, False),
        (6, False),
        (7, False),
        (8, False),
        (9, False),
        (10, False),
        (15, False),
        (17, False),
        (20, False),
        (63, False),
        (65, False),
        (-1, False),
        (-4, False),
        (-16, False),
        (100, False),
        (1000, False),
        (10000, False),
        (2**30, False),  #Large number not power of 4
        (2**32, False), #Large number not power of 4
        (4**10, True), #Large power of 4
        (4**5, True),  #Another large power of 4
        (3.14, False), #Float
        (4.0, True), #Float representing power of 4
        (-3.14, False), #Negative Float
        ("4", False), #String
        ("abc", False), #String
        (None, False), #None
        (True, False), #Boolean
        (False, False), #Boolean

        #Edge cases
        (float('inf'), False),
        (float('-inf'), False),
        (float('nan'), False),
        #Test with very large numbers:
        (4**15, True),
        (4**16, True),
        (4**17, True),

        #Additional test cases to cover a wider range
        (1048576, True),
        (262144, True),
        (65536, True),
        (16384, True),
        (4096, True),
        (1024, True),
        (256, True),
        (64, True),
        (16, True),
        (4, True),
        (1, True),
        (524288, True),
        (2097152, True),
        (8388608,True)



    ],
)
def test_isPowerOfFour(n, expected):
    assert isPowerOfFour(n) == expected
