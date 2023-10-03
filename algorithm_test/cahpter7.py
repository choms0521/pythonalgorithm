def two_sum(number_list: list[int], target: int) -> list:
    try:
        num_dict = {}

        for key, value in enumerate(number_list):
            if target - value in num_dict:
                return [num_dict[target - value], key]

            num_dict[value] = key

    except Exception as e:
        print(e)

    pass


def trapping_rain_water(heights: list[int]) -> int:
    max_height = max(heights)
    max_height_index = heights.index(max_height)

    left_index, right_index = 0, len(heights) - 1
    left_max_height, right_max_height = -1, -1

    water_sum = 0

    while left_index < max_height_index or right_index > max_height_index:
        if left_index < max_height_index:
            if heights[left_index] > left_max_height:
                left_max_height = heights[left_index]
            else:
                water_sum += left_max_height - heights[left_index]

            left_index += 1

        if right_index > max_height_index:
            if heights[right_index] > right_max_height:
                right_max_height = heights[right_index]
            else:
                water_sum += right_max_height - heights[right_index]

            right_index -= 1

    return water_sum


def trapping_rain_water_stack(heights: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(heights)):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            water = min(heights[i], heights[stack[-1]]) - heights[top]

            volume += distance * water

        stack.append(i)

    return volume


def get_sum_two_points(nums: list[int], exclude: int) -> list[list[int]]:
    left_index, right_index = 0, len(nums) - 1
    final_result = []

    while left_index < right_index:
        if nums[left_index] + nums[right_index] == -exclude:
            final_result.append([exclude, nums[left_index], nums[right_index]])
            left_index += 1
            right_index -= 1
        elif nums[left_index] + nums[right_index] < -exclude:
            left_index += 1
        else:
            right_index -= 1

    return final_result


def sum_3(nums: list[int]) -> list[list[int]]:
    sorted_list = sorted(nums)

    final_result = []

    for i in range(len(sorted_list)):
        if i > 0 and sorted_list[i] == sorted_list[i - 1]:
            continue
        temp_list = get_sum_two_points(sorted_list[i + 1 :], sorted_list[i])
        if temp_list:
            final_result.extend(temp_list)
    final_result.reverse()
    return final_result


def array_partion(nums: list[int]) -> int:
    return sum([x for key, x in enumerate(sorted(nums)) if key % 2 == 0])


def product_array_exept_self_bad(nums: list[int]) -> list[int]:
    # [1,2,3,4] => [24, 12, 8, 6]

    left_multiple = []
    right_multiple = []

    for i in range(len(nums)):
        right_index = len(nums) - 1 - i

        if not left_multiple:
            left_multiple.append(nums[i])
        else:
            left_multiple.append(left_multiple[-1] * nums[i])

        if not right_multiple:
            right_multiple.append(nums[right_index])
        else:
            right_multiple.append(right_multiple[-1] * nums[right_index])

    right_multiple.reverse()

    final_result = []
    for i in range(len(left_multiple)):
        if i == 0:
            final_result.append(right_multiple[i + 1])

        elif i == len(left_multiple) - 1:
            final_result.append(left_multiple[i - 1])

        else:
            final_result.append(left_multiple[i - 1] * right_multiple[i + 1])

    return final_result


def product_array_exept_self(nums: list[int]) -> list[int]:
    # [1,2,3,4] => [24, 12, 8, 6]

    out = []

    p = 1

    for i in range(0, len(nums)):
        out.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] *= p
        p *= nums[i]

    return out


def best_time_to_buy_and_sell_stock(prices: list[int]) -> int:
    max_income = prices[1] - prices[0]
    min_value = prices[0]
    for value in prices:
        if value - min_value > max_income:
            max_income = value - min_value

        if value < min_value:
            min_value = value

    return max_income
