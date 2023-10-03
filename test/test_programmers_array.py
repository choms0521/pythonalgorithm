from algorithm_test.pragrammers_array import (
    get_star_points,
    roate_matrix_outline,
    triangle_snails,
    triangle_snails_iteration,
    triangle_snails_angle,
    check_distance,
    matrix_multipliaction,
)


# def test_get_star_points():
#     result = get_star_points(
#         [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, 12], [5, 8, 12]]
#     )


def test_roate_matrix_outline():
    result = roate_matrix_outline(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])

    assert result == [8, 10, 25]


def test_roate_matrix_outline_2():
    result = roate_matrix_outline(
        3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
    )

    assert result == [1, 1, 5, 3]


def test_triangle_snails():
    result = triangle_snails(7, 1)

    assert result == [
        [1],
        [2, 18],
        [3, 19, 17],
        [4, 20, 27, 16],
        [5, 21, 28, 26, 15],
        [6, 22, 23, 24, 25, 14],
        [7, 8, 9, 10, 11, 12, 13],
    ]


def test_triangle_snails_2():
    result = triangle_snails_iteration(7)

    assert result == [
        1,
        2,
        18,
        3,
        19,
        17,
        4,
        20,
        27,
        16,
        5,
        21,
        28,
        26,
        15,
        6,
        22,
        23,
        24,
        25,
        14,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
    ]


def test_triangle_snails_3():
    result = triangle_snails_angle(7)

    assert result == [
        1,
        2,
        18,
        3,
        19,
        17,
        4,
        20,
        27,
        16,
        5,
        21,
        28,
        26,
        15,
        6,
        22,
        23,
        24,
        25,
        14,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
    ]


def test_check_distance():
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]

    result = check_distance(places)

    assert result == [1, 0, 1, 1, 1]


def test_matrix_multipliaction():
    result = matrix_multipliaction([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])

    assert result == [
        [
            15,
            15,
        ],
        [15, 15],
        [15, 15],
    ]


def test_matrix_multipliaction_2():
    result = matrix_multipliaction(
        [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    )

    assert result == [
        [22, 22, 11],
        [36, 28, 18],
        [29, 20, 14],
    ]
