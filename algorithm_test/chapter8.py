from algorithm_test.data_structure.basic_list import BasicList, ListNode


def palindrome_linked_list_with_stack(lists: BasicList) -> bool:
    """먼저 순회를 하면서 스택에 넣고 비교해본다."""

    stack = []

    lists.first()

    while True:
        cur_node = lists.next()

        if cur_node is None:
            break

        stack.append(cur_node.item)

    lists.first()
    while True:
        cur_node = lists.next()

        if cur_node is None:
            break

        top = stack.pop()

        if top != cur_node.item:
            return False

    return True


def palindrome_linked_list_with_runner(lists: BasicList) -> bool:
    """역방향 연결리스트를 만들면서 진행해본다"""

    head = lists.get_head()

    slow_runner, fast_runner = head.next, head.next.next
    slow_runner.rev = head
    rev_runner = None

    while True:
        if fast_runner is None:
            # 홀수일경우 끝까지 도달
            rev_runner = slow_runner.rev
            slow_runner = slow_runner.next

            break
        elif fast_runner.next is None:
            rev_runner = slow_runner
            slow_runner = slow_runner.next
            break

        prior_node = slow_runner
        slow_runner = slow_runner.next  # 역방향 참조를 하면서 리스트를 1칸식 순회한다
        slow_runner.rev = prior_node
        fast_runner = fast_runner.next.next  # 빠른 러너는 두칸씩 순회한다.

    while rev_runner.item != "dummy" and slow_runner is not None:
        if rev_runner.item != slow_runner.item:
            return False

        rev_runner, slow_runner = rev_runner.rev, slow_runner.next

    return True


def merge_two_sorted_lists(sorted_1: BasicList, sorted_2: BasicList) -> BasicList:
    head_1, head_2 = sorted_1.get_head().next, sorted_2.get_head().next

    merge_lists = BasicList()
    merge_head = merge_lists.get_head()
    merge_curr = merge_head

    while head_1 is not None and head_2 is not None:
        if head_1.item < head_2.item:
            new_node = ListNode(head_1.item)
            merge_curr.next = new_node
            merge_curr = merge_curr.next
            head_1 = head_1.next
        else:
            new_node = ListNode(head_2.item)
            merge_curr.next = new_node
            merge_curr = merge_curr.next
            head_2 = head_2.next

    while head_1 is not None:
        new_node = ListNode(head_1.item)
        merge_curr.next = new_node
        merge_curr = merge_curr.next
        head_1 = head_1.next

    while head_2 is not None:
        new_node = ListNode(head_2.item)
        merge_curr.next = new_node
        merge_curr = merge_curr.next
        head_2 = head_2.next

    return merge_lists


def merge_two_sorted_lists_2(sorted_1: BasicList, sorted_2: BasicList) -> BasicList:
    if sorted_2 is None:
        return sorted_1

    head_1, head_2 = sorted_1.get_head(), sorted_2.get_head()

    insert_curr = head_1
    start_head = insert_curr

    head_1 = head_1.next
    head_2 = head_2.next

    while head_1 is not None and head_2 is not None:
        if head_1.item < head_2.item:
            insert_curr.next = head_1
            head_1 = head_1.next

        else:
            insert_curr.next = head_2
            head_2 = head_2.next

        insert_curr = insert_curr.next

    while head_1 is not None:
        insert_curr.next = head_1
        head_1 = head_1.next
        insert_curr = insert_curr.next

    while head_2 is not None:
        insert_curr.next = head_2
        head_2 = head_2.next
        insert_curr = insert_curr.next

    # sorted_1.set_head(start_head)

    return sorted_1


def reverse_linked_list(lists: BasicList) -> None:
    lists.reverse()

    return None
