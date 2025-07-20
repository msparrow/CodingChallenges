import pytest
from solutions.solution_50 import simplify_path

@pytest.mark.parametrize("path, expected", [
    ("/home/", "/home"),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ("/a/./b/../../c/", "/c"),
    ("/a/../../b/../c//.//", "/c"),
    ("/a//b////c/d//././/..", "/a/b/c"),
    ("/...", "/..."),
    ("/.hidden", "/.hidden"),
    ("/..hidden", "/..hidden"),
    ("/file.txt", "/file.txt"),
    ("/dir/./././file", "/dir/file"),
    ("/dir/../dir/file", "/dir/file"),
    ("/a/b/c/../d", "/a/b/d"),
    ("a/b/c", "/a/b/c"),
    ("//a//b//", "/a/b"),
    ("/..", "/"),
    ("/.", "/"),
    ("/", "/"),
    ("/../..", "/"),
    ("/a/./b/.", "/a/b")
])
def test_simplify_path(path, expected):
    assert simplify_path(path) == expected