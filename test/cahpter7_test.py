from algorithm_test.cahpter7 import (
    two_sum,
    trapping_rain_water,
    trapping_rain_water_stack,
    sum_3,
    array_partion,
    product_array_exept_self,
    best_time_to_buy_and_sell_stock,
)


def test_two_sum_1():
    result = two_sum([2, 7, 11, 15], 9)

    assert result == [0, 1]


def test_two_sum_2():
    result = two_sum([2, 7, 11, 15], 22)

    assert result == [1, 3]


def test_two_sum_3():
    result = two_sum([15, 2, 7, 11], 22)

    assert result == [0, 2]


def test_trapping_rain_water():
    result = trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

    assert result == 6


def test_trapping_rain_water_2():
    result = trapping_rain_water([0, 1, 0, 3, 1, 0, 1, 3, 2, 1, 2, 1])

    assert result == 9


def test_trapping_rain_water_stack():
    result = trapping_rain_water_stack([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

    assert result == 6


def test_sum_3():
    result = sum_3([-1, 0, 1, 2, -1, -4])
    print(result)

    assert result == [[-1, 0, 1], [-1, -1, 2]]


def test_array_partion():
    result = array_partion([1, 4, 3, 2])

    assert result == 4


def test_product_array_exept_self():
    result = product_array_exept_self([1, 2, 3, 4])

    assert result == [24, 12, 8, 6]
    # assert result == -1


def test_best_time_to_buy_and_sell_stock():
    restul = best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4])

    assert restul == 5
