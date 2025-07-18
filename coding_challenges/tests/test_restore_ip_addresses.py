
import pytest
from solutions.solution_74 import restore_ip_addresses

@pytest.mark.parametrize("s, expected", [
    ("25525511135", sorted(["255.255.11.135", "255.255.111.35"])),
    ("0000", ["0.0.0.0"]),
    ("101023", sorted(["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]))
])
def test_restore_ip_addresses(s, expected):
    assert sorted(restore_ip_addresses(s)) == expected
