
import pytest
from solutions.solution_36 import group_anagrams

@pytest.mark.parametrize("strs, expected", [
    (["eat","tea","tan","ate","nat","bat"], sorted([sorted(["bat"]),sorted(["nat","tan"]),sorted(["ate","eat","tea"])])),
    ([""], [[""]]),
    (["a"], [["a"]]),
    ([""], [[""]]),
    (["ab", "ba", "abc", "cba"], sorted([sorted(["ab", "ba"]), sorted(["abc", "cba"])])),
    (["listen", "silent", "enlist"], [sorted(["listen", "silent", "enlist"])])
])
def test_group_anagrams(strs, expected):
    result = group_anagrams(strs)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
