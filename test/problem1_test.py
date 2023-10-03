from algorithm_test.problem1 import check_panlindrome


def test_check_panlindrome_problem_1():
    """문제 1-1 테스트하기"""
    result = check_panlindrome("A man, a plan, a canal: Panama")
    if result:
        assert True
    else:
        assert False


def test_check_panlindrome_problem_1__1():
    """실패케이스"""
    result = check_panlindrome("race a car")
    if result:
        assert False
    else:
        assert True
