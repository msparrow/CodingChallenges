
import pytest
from solutions.solution_12 import letter_combinations

@pytest.mark.parametrize("digits, expected", [
    ("23", sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])),
    ("", sorted([])),
    ("2", sorted(["a","b","c"])),
    ("7", sorted(["p","q","r","s"])),
    ("9", sorted(["w","x","y","z"])),
    ("234", sorted(["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"])),
    ("567", sorted(["jmp","jmq","jmr","jms","jnp","jnq","jnr","jns","jop","joq","jor","jos","kmp","kmq","kmr","kms","knp","knq","knr","kns","kop","koq","kor","kos","lmp","lmq","lmr","lms","lnp","lnq","lnr","lns","lop","loq","lor","los"])),
    ("89", sorted(["tw","tx","ty","tz","uw","ux","uy","uz","vw","vx","vy","vz"])),
    ("22", sorted(["aa","ab","ac","ba","bb","bc","ca","cb","cc"])),
    ("99", sorted(["ww","wx","wy","wz","xw","xx","xy","xz","yw","yx","yy","yz","zw","zx","zy","zz"])),
    ("2345", sorted(["adgj", "adgk", "adgl", "adhj", "adhk", "adhl", "adij", "adik", "adil", "aegj", "aegk", "aegl", "aehj", "aehk", "aehl", "aeij", "aeik", "aeil", "afgj", "afgk", "afgl", "afhj", "afhk", "afhl", "afij", "afik", "afil", "bdgj", "bdgk", "bdgl", "bdhj", "bdhk", "bdhl", "bdij", "bdik", "bdil", "begj", "begk", "begl", "behj", "behk", "behl", "beij", "beik", "beil", "bfgj", "bfgk", "bfgl", "bfhj", "bfhk", "bfhl", "bfij", "bfik", "bfil", "cdgj", "cdgk", "cdgl", "cdhj", "cdhk", "cdhl", "cdij", "cdik", "cdil", "cegj", "cegk", "cegl", "cehj", "cehk", "cehl", "ceij", "ceik", "ceil", "cfgj", "cfgk", "cfgl", "cfhj", "cfhk", "cfhl", "cfij", "cfik", "cfil"])) 
])
def test_letter_combinations(digits, expected):
    # Sorting the output to make the test deterministic
    assert sorted(letter_combinations(digits)) == expected
