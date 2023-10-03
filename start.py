import collections
from collections import defaultdict
from DS.LinkedList import LinkedListBasic
import re


def check_palindrome(checkStr: str) -> bool:
    index = 0
    reverse_index = -1
    while index < len(checkStr) and reverse_index >= -len(checkStr):
        while not checkStr[index].isdigit() and not checkStr[index].isalpha():
            index += 1

        while (
            not checkStr[reverse_index].isdigit()
            and not checkStr[reverse_index].isalpha()
        ):
            reverse_index -= 1

        if checkStr[index].lower() != checkStr[reverse_index].lower():
            return False

        if index == reverse_index:
            break

        index += 1
        reverse_index -= 1

    return True


def check_palindrome_with_deque(check_str: str) -> bool:
    deque = collections.deque()

    for char in check_str:
        if char.isalnum():
            deque.append(char.lower())

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False

    return True


def reverse_str_list(change_list: list) -> None:
    # change_list.reverse()

    left_Index = 0

    while left_Index <= len(change_list) - 1 - left_Index:
        change_list[left_Index], change_list[len(change_list) - 1 - left_Index] = (
            change_list[len(change_list) - 1 - left_Index],
            change_list[left_Index],
        )

        left_Index += 1


def reorder_log_files(logs: list[str]) -> list[str]:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits


def get_most_words(words: str, banned_words_list) -> None:
    words_number = defaultdict(int)
    word_list = words.split(" ")
    for word in word_list:
        ref_word = re.sub("[^a-z0-9]", "", word.lower())
        if ref_word not in banned_words_list:
            words_number[ref_word] += 1

    maxValue = 0
    maxKey = ""

    for key, value in words_number.items():
        if value > maxValue:
            maxValue = value
            maxKey = key

    return maxKey


def get_anagram_list(word_list: list[str]) -> list[list[str]]:
    word_dict = defaultdict(list)

    for word in word_list:
        sorted = [w for w in word]
        sorted.sort()

        word_dict["".join(sorted)].append(word)

    print(word_dict)

    return word_dict.values()


def trap(height: list[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


def trap_stack(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만난다.
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume


def calc_three_number(num_list: list[int]) -> list:
    final_list = []
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            for k in range(j + 1, len(num_list)):
                if num_list[i] + num_list[j] + num_list[k] == 0:
                    final_list.append([num_list[i], num_list[j], num_list[k]])

    return final_list


def partition_array(num_list: list[int]) -> int:
    num_list.sort(reverse=True)

    sum = 0

    index = 0
    while index < len(num_list) // 2 * 2 - 1:
        sum += min(num_list[index], num_list[index + 1])
        index += 2

    return sum


def product_of_array_except_self(num_list: list[int]) -> list[int]:
    out = []
    right_out = []
    final_result = []

    for i in range(len(num_list)):
        if not out:
            out.append(1)

        else:
            out.append(out[-1] * num_list[i - 1])

        if not right_out:
            right_out.insert(0, 1)
        else:
            right_out.insert(0, right_out[0] * num_list[len(num_list) - i])

    for i in range(len(out)):
        final_result.append(out[i] * right_out[i])

    return final_result


def sum_two_list(list_1: LinkedListBasic, list_2: LinkedListBasic) -> int:
    result = 0
    carry = 0

    fisrt_value_list_1 = list_1.initialize_pos()
    first_value_list_2 = list_2.initialize_pos()

    index = 0
    while fisrt_value_list_1 is not None or first_value_list_2 is not None:
        sum = 0

        if fisrt_value_list_1 is not None:
            sum += fisrt_value_list_1
            fisrt_value_list_1 = list_1.next()

        if first_value_list_2 is not None:
            sum += first_value_list_2
            first_value_list_2 = list_2.next()

            carry, sum = divmod(sum + carry, 10)

        result += sum * pow(10, index)

        index += 1

    return result


if __name__ == "__main__":
    l1 = LinkedListBasic()
    l2 = LinkedListBasic()

    l1.insert(0, 7)
    l1.insert(0, 4)
    l1.insert(0, 6)
    l1.insert(0, 5)
    l1.insert(0, 3)
    l1.insert(0, 1)
    l1.insert(0, 2)

    l1.odd_even_linked_list()

    l1.printList()
