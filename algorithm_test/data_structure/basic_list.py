class ListNode:
    """연결리스트 노드"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.rev = None


class BasicList:
    """단순 단방향 연결리스트"""

    def __init__(self):
        """더미노드를 만든다"""
        self.__head = ListNode("dummy")
        self.__curr = None

    def insert(self, x):
        """맨앞에 넣는걸로 구현"""

        first_node = self.__head.next

        new_node = ListNode(x)
        self.__head.next = new_node
        new_node.next = first_node

    def first(self):
        self.__curr = self.__head
        return self.__curr

    def next(self):
        self.__curr = self.__curr.next

        return self.__curr

    def get_head(self):
        return self.__head

    def print_all(self):
        curr = self.__head.next
        while curr is not None:
            print(curr.item, sep="-")
            curr = curr.next

    def set_head(self, head: ListNode) -> None:
        self.__head = head

    def __reverse(self, cur_node: ListNode) -> ListNode:
        print("call")
        if cur_node.next is None:
            self.__head.next = cur_node
            return cur_node

        next_node = self.__reverse(cur_node.next)
        next_node.next = cur_node

        return cur_node

    def reverse(self) -> None:
        curr = self.__reverse(self.__head.next)
        curr.next = None
        print("here")
