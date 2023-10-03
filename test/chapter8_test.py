from algorithm_test.data_structure.basic_list import BasicList
from algorithm_test.chapter8 import (
    palindrome_linked_list_with_stack,
    palindrome_linked_list_with_runner,
)


def test_palindrome_linked_list():
    made_lists = BasicList()

    made_lists.insert(2)
    made_lists.insert(1)

    result = palindrome_linked_list_with_stack(made_lists)

    if result:
        assert False
    else:
        assert True


def test_palindrome_linked_list_2():
    made_lists = BasicList()

    made_lists.insert(1)
    made_lists.insert(2)
    made_lists.insert(2)
    made_lists.insert(1)

    result = palindrome_linked_list_with_stack(made_lists)

    if result:
        assert True
    else:
        assert False


def test_palindrome_linked_list_with_runner():
    made_lists = BasicList()

    made_lists.insert(2)
    made_lists.insert(1)

    result = palindrome_linked_list_with_runner(made_lists)

    if result:
        assert False
    else:
        assert True


def test_palindrome_linked_list_with_runner_2():
    made_lists = BasicList()

    made_lists.insert(1)
    made_lists.insert(2)
    made_lists.insert(2)
    made_lists.insert(1)

    result = palindrome_linked_list_with_runner(made_lists)

    if result:
        assert True
    else:
        assert False


def test_palindrome_linked_list_with_runner_3():
    made_lists = BasicList()

    made_lists.insert(1)
    made_lists.insert(2)
    made_lists.insert(3)
    made_lists.insert(4)
    made_lists.insert(5)
    made_lists.insert(6)
    made_lists.insert(7)
    made_lists.insert(8)
    made_lists.insert(7)
    made_lists.insert(6)
    made_lists.insert(5)
    made_lists.insert(4)
    made_lists.insert(3)
    made_lists.insert(2)
    made_lists.insert(1)

    result = palindrome_linked_list_with_runner(made_lists)

    if result:
        assert True
    else:
        assert False


def test_palindrome_linked_list_with_runner_4():
    made_lists = BasicList()

    made_lists.insert(1)
    made_lists.insert(2)
    made_lists.insert(3)
    made_lists.insert(4)
    made_lists.insert(5)
    made_lists.insert(6)
    made_lists.insert(7)
    made_lists.insert(7)
    made_lists.insert(6)
    made_lists.insert(5)
    made_lists.insert(4)
    made_lists.insert(3)
    made_lists.insert(2)
    made_lists.insert(1)

    result = palindrome_linked_list_with_runner(made_lists)

    if result:
        assert True
    else:
        assert False


def test_palindrome_linked_list_with_runner_5():
    made_lists = BasicList()

    made_lists.insert(1)
    made_lists.insert(2)
    made_lists.insert(3)
    made_lists.insert(4)
    made_lists.insert(5)
    made_lists.insert(6)
    made_lists.insert(7)
    made_lists.insert(7)
    made_lists.insert(6)
    made_lists.insert(5)
    made_lists.insert(4)
    made_lists.insert(3)

    result = palindrome_linked_list_with_runner(made_lists)

    if result:
        assert False
    else:
        assert True
