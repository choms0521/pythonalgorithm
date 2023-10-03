def order_func(value: str) -> tuple:
    str_list = value.split(" ")

    first_value = 0

    if str_list[1].isnumeric():
        first_value = 1

    return first_value, str_list[0]


def reorder_logs(logs: list) -> list:
    """로그를 재정렬한다."""

    letters = []
    digits = []

    for log in logs:
        split_log = log.split(" ")

        if split_log[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

        letters.sort(key=lambda letter: (letter.split(" ")[1:], letter.split(" ")[0]))

    return letters + digits


# 정규표현식을 배우고 다시오자!!
def most_common_word(words: str, exclude_words: list[str]) -> str:
    pass


def group_anagrams(words: list[str]):
    result_dict = {}

    for word in words:
        key = "".join(sorted(word))
        if result_dict.get(key):
            result_dict[key].append(word)
        else:
            result_dict[key] = []
            result_dict[key].append(word)

    return list(result_dict.values())


# def longest_palindrome_substring(default_string: str) -> str:
#     """주어진 문자열에서 만들 수 있는 가장 긴 팰린드롬 반환하기"""

#     reverse_string = [s for s in default_string[::-1]]

#     index = 0

#     final_palindrome = ""
#     while index < len(default_string):
#         if reverse_string[index] == default_string[index]:
#             panlindrome_candidate = default_string[index]
#             index += 1

#             while (
#                 index < len(default_string)
#                 and reverse_string[index] == default_string[index]
#             ):
#                 panlindrome_candidate += default_string[index]
#                 index += 1

#             if len(panlindrome_candidate) > len(final_palindrome):
#                 final_palindrome = panlindrome_candidate

#         index += 1

#     return final_palindrome


def longest_palindrome_substring(default_string: str) -> str:
    """주어진 문자열에서 만들 수 있는 가장 긴 팰린드롬 반환하기"""

    if len(default_string) < 2 or default_string == default_string[::-1]:
        return default_string

    index = 0

    final_palindrome = ""
    while index < len(default_string):
        if index + 2 < len(default_string):
            if default_string[index] == default_string[index + 2]:
                palindrome_candidate = default_string[index : index + 3]
                plus_index = 1
                while (
                    index - plus_index >= 0
                    and index + 2 + plus_index < len(default_string)
                    and default_string[index - plus_index]
                    == default_string[index + 2 + plus_index]
                ):
                    palindrome_candidate = (
                        default_string[index - plus_index]
                        + palindrome_candidate
                        + default_string[index + 2 + plus_index]
                    )
                    plus_index += 1

                if len(palindrome_candidate) > len(final_palindrome):
                    final_palindrome = palindrome_candidate

        if index + 1 < len(default_string):
            if default_string[index] == default_string[index + 1]:
                palindrome_candidate = default_string[index : index + 2]
                plus_index = 1
                while (
                    index - plus_index >= 0
                    and index + 1 + plus_index < len(default_string)
                    and default_string[index - plus_index]
                    == default_string[index + 1 + plus_index]
                ):
                    palindrome_candidate = (
                        default_string[index - plus_index]
                        + palindrome_candidate
                        + default_string[index + 1 + plus_index]
                    )
                    plus_index += 1

                if len(palindrome_candidate) > len(final_palindrome):
                    final_palindrome = palindrome_candidate

        index += 1

    return final_palindrome
