def seizer_scret(original: str, n: int) -> str:
    max_num_lower = ord("z")
    max_num_upper = ord("Z")

    result = []
    for s in original:
        if s.isalpha():
            if s.lower() == s:  # 소문자라면
                new_num = ord(s) + n

                if new_num > max_num_lower:
                    new_num -= 26

                result.append(chr(new_num))

            else:
                new_num = ord(s) + n

                if new_num > max_num_upper:
                    new_num -= 26

                result.append(chr(new_num))

        else:
            result.append(s)

    return "".join(result)


def wired_string_1(words: str) -> str:
    word_list = words.split(" ")

    final_list = []
    for word in word_list:
        new_words = []
        for i in range(len(word)):
            if i % 2 == 0:
                new_words.append(word[i].upper())
            else:
                new_words.append(word[i].lower())

        final_list.append("".join(new_words))

    return " ".join(final_list)


def tuple_string_1(words: str) -> list[int]:
    new_list = []

    stack = []

    for s in words[1:-1]:
        if s == "{" or s == " " or s == ",":
            continue
        elif s == "}":
            words_list = []
            for i in range(len(stack)):
                words_list.append(stack[i])
            new_list.append(words_list)
            stack = []
        else:
            stack.append(s)

    final_value = []

    new_list.sort(key=lambda x: len(x))

    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if int(new_list[i][j]) not in final_value:
                final_value.append(int(new_list[i][j]))
                break

    return final_value


def tuple_string_another(words: str) -> list[int]:
    answer = {}

    words = words.replace(" ", "")
    s = sorted(words[2:-2].split("},{"), key=len)

    for tuples in s:
        elements = tuples.split(",")
        for element in elements:
            number = int(element)
            if number not in answer:
                answer[number] = 1

    # 딕셔너리에 저장하면 정렬은 필요없을 것 같다. 다만 n2 아래부분 개선이 가능한가?

    return list(answer)


def remove_couple_string(words: str) -> int:
    stack = []
    for i in range(len(words)):
        if len(stack) == 0:
            stack.append(words[i])

        else:
            top = stack[-1]
            if top == words[i]:
                stack.pop()
            else:
                stack.append(words[i])

    if len(stack) > 0:
        return 0

    else:
        return 1


def compress_string_level_1(words: str) -> int:
    words_length = len(words)

    min_length = words_length

    for i in range(1, words_length // 2 + 1):
        compressed_str = ""
        if words_length % i == 0:
            # 해당 문자열로 쪼갤 수 있다.
            j = 0
            while j <= words_length - i:
                if j == words_length - i - 1:
                    compressed_str += words[j : j + i]
                    break

                number = 1
                insert_str = words[j : j + i]

                if words[j : j + i] == words[j + i : j + 2 * i]:
                    while words[j : j + i] == words[j + i : j + 2 * i]:
                        j += i
                        number += 1

                    compressed_str += str(number)
                    compressed_str += insert_str
                    j += i

                else:
                    compressed_str += insert_str
                    j += i

            if len(compressed_str) < min_length:
                min_length = len(compressed_str)

    return min_length
