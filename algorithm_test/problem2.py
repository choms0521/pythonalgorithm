def get_reverse_string(in_str: list) -> None:
    """들어온 문자열을 뒤집는다"""

    start_index = 0
    end_index = len(in_str) - 1
    while start_index < end_index:
        in_str[start_index], in_str[end_index] = in_str[end_index], in_str[start_index]
        start_index += 1
        end_index -= 1
