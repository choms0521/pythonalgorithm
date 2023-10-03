def get_star_points(equations: list[list[int]]):
    # 각변이 최대 1000이다.

    star_positions = []

    try:
        # 직선 두개가 점하나를 만들 수 있다.
        for i in range(len(equations)):
            for j in range(i + 1, len(equations)):
                y_position = -(
                    equations[i][2] * equations[j][0]
                    - equations[j][2] * equations[i][0]
                ) / (
                    equations[i][1] * equations[j][0]
                    - equations[j][1] * equations[i][0]
                )

                if equations[i][0] != 0:
                    x_position = (
                        -(equations[i][1] * y_position + equations[i][2])
                        / equations[i][0]
                    )

                else:
                    x_position = (
                        -(equations[j][1] * y_position + equations[j][2])
                        / equations[j][0]
                    )

                if x_position == int(x_position) and y_position == int(y_position):
                    print(x_position, y_position)
                    star_positions.append([int(x_position), int(y_position)])

        print("the end!!")
    except Exception:
        print(i, j)

    print("testing")


def roate_matrix_outline(rows: int, cols: int, queryies: list[int]):
    # 기준 행렬을 만든다.

    default_matrix = []

    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(i * cols + j + 1)
        default_matrix.append(new_row)

    # 주어진 회전 조건에 따라 2차원 배열을 회전시킨다.

    fianl_result = []

    for query in queryies:
        x_index = [query[0] - 1, query[2] - 1]
        y_index = [query[1] - 1, query[3] - 1]

        # 테두리를 회전시킨다. (함수 분리 가능)
        change_value = default_matrix[x_index[0]][y_index[0]]
        min_value = change_value
        # 상단
        for x in range(y_index[0] + 1, y_index[1] + 1):
            # temp_value = default_matrix[x_index[0]][x]
            # default_matrix[x_index[0]][x] = change_value
            # change_value = temp_value
            default_matrix[x_index[0]][x], change_value = (
                change_value,
                default_matrix[x_index[0]][x],
            )

            if change_value < min_value:
                min_value = change_value

        # 오른쪽

        for y in range(x_index[0] + 1, x_index[1] + 1):
            default_matrix[y][y_index[1]], change_value = (
                change_value,
                default_matrix[y][y_index[1]],
            )

            if change_value < min_value:
                min_value = change_value

        # 하단
        for x in range(y_index[1] - 1, y_index[0] - 1, -1):
            # temp_value = change_value = default_matrix[x_index[1]][x + 1]
            # default_matrix[x_index[1]][x + 1] = default_matrix[x_index[1]][x]
            # change_value = temp_value

            default_matrix[x_index[1]][x], change_value = (
                change_value,
                default_matrix[x_index[1]][x],
            )

            if change_value < min_value:
                min_value = change_value
        # 왼쪽
        for y in range(x_index[1] - 1, x_index[0] - 1, -1):
            # temp_value = change_value = default_matrix[y - 1][x_index[0]]
            # default_matrix[y - 1][x_index[0]] = default_matrix[y][x_index[0]]
            # change_value = temp_value

            default_matrix[y][x_index[0]], change_value = (
                change_value,
                default_matrix[y][x_index[0]],
            )
            if change_value < min_value:
                min_value = change_value

        fianl_result.append(min_value)

    return fianl_result


def triangle_snails(height: int, start_number: int) -> list[int]:
    final_list = []

    if height <= 1:
        return [[start_number]]
    elif height == 2:
        return [
            [start_number],
            [
                start_number + 1,
                start_number + 2,
            ],
        ]

    elif height == 3:
        return [
            [start_number],
            [start_number + 1, start_number + 5],
            [start_number + 2, start_number + 3, start_number + 4],
        ]

    insert_number = start_number
    for i in range(height - 1):
        new_list = [insert_number]
        final_list.append(new_list)
        insert_number += 1

    final_list.append([])
    for i in range(height):
        final_list[height - 1].append(insert_number)
        insert_number += 1

    for i in range(height - 2, 0, -1):
        final_list[i].append(insert_number)
        insert_number += 1

    inner_snail = triangle_snails(height - 3, insert_number)

    # 내부 스네일 삽입하기

    for i in range(height - 3):
        final_list[i + 2][1 : len(final_list[i + 2]) - 1] = inner_snail[i]

    return final_list


def triangle_snails_iteration(height: int) -> list[int]:
    two_array_list = [[0] * (i + 1) for i in range(height)]

    row_idx, col_idx = 0, 0
    insert_number = 1

    while True:
        if two_array_list[row_idx][col_idx] != 0:
            break

        # 아래로 내려가기
        while row_idx < height - 1:
            two_array_list[row_idx][col_idx] = insert_number
            insert_number += 1
            row_idx += 1

            if row_idx == height - 1 or two_array_list[row_idx + 1][col_idx] != 0:
                break

        if two_array_list[row_idx][col_idx] != 0:
            break

        # 오른쪽으로 이동하기
        while col_idx < len(two_array_list[row_idx]) - 1:
            two_array_list[row_idx][col_idx] = insert_number
            insert_number += 1
            col_idx += 1

            if (
                col_idx == len(two_array_list[row_idx]) - 1
                or two_array_list[row_idx][col_idx + 1] != 0
            ):
                break

        if two_array_list[row_idx][col_idx] != 0:
            break

        # 대각선 이동
        while row_idx > 0 and col_idx > 0:
            two_array_list[row_idx][col_idx] = insert_number
            insert_number += 1
            col_idx -= 1
            row_idx -= 1

            if two_array_list[row_idx - 1][col_idx - 1] != 0:
                break

    final_list = []

    for rows in two_array_list:
        for value in rows:
            final_list.append(value)

    return final_list


def triangle_snails_angle(height: int) -> list[int]:
    res = [[0] * i for i in range(1, height + 1)]

    row_idx, col_idx = -1, 0
    insert_number = 1

    for i in range(height):
        for _ in range(i, height):
            angle = i % 3

            if angle == 0:
                row_idx += 1
            elif angle == 1:
                col_idx += 1
            else:
                row_idx -= 1
                col_idx -= 1

            res[row_idx][col_idx] = insert_number
            insert_number += 1

    return [x for rows in res for x in rows]


def check_test_places(room: list[list[str]]) -> int:
    for i in range(5):
        for j in range(5 - i):
            # 문제가 될 수 있는 지점 3군데 오른쪽으로 두칸 옆, 아래로 두칸 밑, 대각선 한칸

            if room[i][j] != "P":
                continue

            test_row_index, test_col_index = i + 2, j

            # 아래쪽 거리 확인

            if test_row_index < 5 and test_col_index < 5:
                if (
                    room[test_row_index][test_col_index] == "P"
                    and room[test_row_index - 1][test_col_index] != "X"
                ):
                    return 0

            # 오른쪽 거래 확인

            test_row_index, test_col_index = i, j + 2

            if test_row_index < 5 and test_col_index < 5:
                if (
                    room[test_row_index][test_col_index] == "P"
                    and room[test_row_index][test_col_index - 1] != "X"
                ):
                    return 0

            # 대각선 확인
            test_row_index, test_col_index = i + 1, j + 1

            if test_row_index < 5 and test_col_index < 5:
                if room[test_row_index][test_col_index] == "P" and (
                    room[test_row_index][test_col_index - 1] != "X"
                    or room[test_row_index - 1][test_col_index] != "X"
                ):
                    return 0

            # 바로 오른쪽
            test_row_index, test_col_index = i, j + 1
            if test_row_index < 5 and test_col_index < 5:
                if room[test_row_index][test_col_index] == "P":
                    return 0

            # 바로 아래쪽

            test_row_index, test_col_index = i + 1, j
            if test_row_index < 5 and test_col_index < 5:
                if room[test_row_index][test_col_index] == "P":
                    return 0

    return 1


def check_distance(place_info: list[list[str]]) -> list[int]:
    final_result = []
    for room in place_info:
        places = [[partition for partition in row] for row in room]
        final_result.append(check_test_places(places))

    return final_result


def matrix_multipliaction(
    matrix_a: list[list[int]], matirx_b: list[list[int]]
) -> list[list[int]]:
    if len(matrix_a[0]) != len(matirx_b):
        return None

    final_result = []
    for i in range(len(matrix_a)):
        new_row = []

        for j in range(len(matirx_b)):
            sum = 0
            for k in range(len(matrix_a[0])):
                sum += matrix_a[i][k] * matirx_b[k][j]

            new_row.append(sum)

        final_result.append(new_row)

    return final_result
