def check_panlindrome(check_str: str) -> bool:
    """해당 문자열이 팰린드롬인지 확인하기(영문, 숫자만 따진다.)"""
    changed_list = [s.lower() for s in check_str if s.isalnum()]

    start_index = 0
    end_index = len(changed_list) - 1

    while start_index < end_index:
        if changed_list[start_index] != changed_list[end_index]:
            return False

        start_index += 1
        end_index -= 1

    return True
