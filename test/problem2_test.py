from algorithm_test.problem2 import get_reverse_string
from algorithm_test.chapter6 import (
    reorder_logs,
    group_anagrams,
    longest_palindrome_substring,
)


def test_problem_2_1():
    ref_str = ["h", "e", "l", "l", "o"]

    get_reverse_string(ref_str)

    assert ref_str == ["o", "l", "l", "e", "h"]


def test_reorder_logs():
    test_case = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]

    result = reorder_logs(test_case)

    assert result == [
        "let1 art can",
        "let3 art zero",
        "let2 own kit dig",
        "dig1 8 1 5 1",
        "dig2 3 6",
    ]


def test_group_anagrams():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    assert result == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


def test_longest_palindrome_substring_1():
    result = longest_palindrome_substring("babad")

    assert result == "bab"


def test_longest_palindrome_substring_2():
    result = longest_palindrome_substring("a")

    assert result == "a"


def test_longest_palindrome_substring_3():
    result = longest_palindrome_substring("1234565432")

    assert result == "234565432"
