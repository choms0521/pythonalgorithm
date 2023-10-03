from algorithm_test.programmers_string import (
    seizer_scret,
    wired_string_1,
    tuple_string_1,
    tuple_string_another,
    remove_couple_string,
    compress_string_level_1,
)


def test_seizer_scret():
    result = seizer_scret("AB", 1)

    assert result == "BC"


def test_seizer_scret_2():
    result = seizer_scret("z", 1)

    assert result == "a"


def test_seizer_scret_3():
    result = seizer_scret("Z B z", 2)

    assert result == "B D b"


def test_wired_string_1():
    result = wired_string_1("try hello world")

    assert result == "TrY HeLlO WoRlD"


def test_tuple_string_1():
    result = tuple_string_1("{{2},  {2,1}, {2,1,3}, {2,1,3,4}}")

    assert result == [2, 1, 3, 4]


def test_tuple_string_2():
    result = tuple_string_1("{{4,2,3},  {3}, {2,3,4,1}, {2,3}}")

    assert result == [3, 2, 4, 1]


def test_tuple_string_another():
    result = tuple_string_another("{{4,2,3},  {3}, {2,3,4,1}, {2,3}}")

    assert result == [3, 2, 4, 1]


def test_remove_couple_string():
    result = remove_couple_string("baabaa")

    assert result == 1


def test_remove_couple_string_2():
    result = remove_couple_string("cdcd")

    assert result == 0


def test_compress_string_level_1():
    result = compress_string_level_1("aabbaccc")

    assert result == 7


def test_compress_string_level_2():
    result = compress_string_level_1("abcabcabcabcdededededede")

    assert result == 14
