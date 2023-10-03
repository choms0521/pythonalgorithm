class ListNode:
    def __init__(self, newItem, nextNode: "ListNode"):
        self.item = newItem
        self.next = nextNode


class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
        self.__cur_pos = self.__head.next

    def __getNode(self, i) -> ListNode:
        curr = self.__head
        for index in range(i + 1):
            curr = curr.next

        return curr

    def getNodeOut(self, i) -> ListNode:
        curr = self.__head
        for index in range(i + 1):
            curr = curr.next

        return curr

    def insert(self, i: int, x):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)
            newNode = ListNode(x, prev.next)
            prev.next = newNode
            self.__numItems += 1

        else:
            print("outofboxerror")

    def append(self, x):
        prev = self.__getNode(self.__numItems - 1)
        newNode = ListNode(x, prev.next)
        prev.next = newNode
        self.__numItems += 1

    def __findNode(self, x) -> (ListNode, ListNode):
        prev = self.__head
        curr = prev.next

        while curr is not None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr
                curr = prev.next

        return (None, None)

    def pop(self, *args):
        if self.isEmpty():
            return None

        i = -1

        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems - 1

        if i >= 0 and i < self.__numItems:
            prev = self.__getNode(i - 1)
            curr = prev.next

            item = curr.item

            prev.next = curr.next
            self.__numItems -= 1

            return item
        else:
            return None

    def remove(self, x):
        (prev, curr) = self.__findNode(x)

        if curr is not None:
            prev.next = curr.next
            self.__numItems -= 1

    def get(self, i):
        if self.isEmpty():
            return None

        if i >= 0 and i < self.__numItems:
            curr = self.__getNode(i)
            return curr.item
        else:
            return None

    def index(self, x):
        curr = self.__head

        for i in range(self.__numItems):
            curr = curr.next
            if curr.item == x:
                return i

        return -1

    def isEmpty(self):
        return self.__numItems == 0

    def size(self):
        return self.__numItems

    def clear(self, x):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0

    def count(self, x):
        curr = self.__head

        count = 0
        for i in range(self.__numItems):
            curr = curr.next
            if curr.item == x:
                count += 1

        return count

    def extend(self, a):
        for i in range(a.size()):
            self.append(a.get(i))

    def copy(self):
        copyList = LinkedListBasic()

        for index in range(self.__numItems):
            copyList.append(self.get(index))

        return copyList

    def reverse(self):
        a = LinkedListBasic()

        for index in range(self.__numItems):
            a.insert(0, self.get(index))

        self.clear()

        for index in range(a.size()):
            self.append(a.get(index))

    def sort(self) -> None:
        a = []

        for index in range(self.__numItems):
            a.append(0, self.get(index))

        a.sort()

        self.clear()
        for index in range(len(a)):
            self.append(a[index])

    def printList(self) -> None:
        curr = self.__head.next

        while curr is not None:
            print(curr.item, end=" ")
            curr = curr.next

        print()

    def printInterval(self, i: int, j: int):
        startNode = self.__getNode(i)

        for index in range(0, j - i + 1):
            print(startNode.item)
            startNode = startNode.next

        print()

    # def numItems(self):
    #     curr = self.__head.next
    #     cnt = 0
    #     while True:
    #         if curr == None:
    #             break

    #         curr = curr.next
    #         cnt += 1

    #     return cnt

    def numItems(self):
        return self.numItemsRecursion(self.__head.next)

    def numItemsRecursion(self, startNode):
        if startNode is None:
            return 0

        sum = 1 + self.numItemsRecursion(startNode.next)

        return sum

    # def pop(self, i: int, k: int):
    #     if i >= self.__numItems:
    #         return None

    #     prevNode = self.__getNode(i - 1)

    #     finalNode = prevNode.next

    #     deleteNum = 0
    #     for index in range(0, k - 1):
    #         if finalNode == None:
    #             break

    #         finalNode = finalNode.next
    #         deleteNum += 1

    #     if finalNode != None:
    #         nextNode = finalNode.next
    #         prevNode.next = nextNode
    #         self.__numItems -= deleteNum

    def __iter__(self):
        return LinkedListBasicIterator(self)

    def lastIndexOf(self, x) -> int:
        curr = self.__head

        lastIndex = None
        cnt = 0
        while curr.next is None:
            curr = curr.next
            if curr.item == x:
                lastIndex = cnt

            cnt += 1

        return lastIndex

    def reverse_new(self):
        prev = None
        curr = self.__head.next

        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next

        self.__head.next = prev

    def reverse_recursion(self, prev, curr):
        if curr is None:
            return prev

        curr.next, prev, curr = prev, curr, curr.next

        return self.reverse_recursion(prev, curr)

    def reverse_2(self):
        startNode = self.reverse_recursion(None, self.__head.next)

        self.__head.next = startNode

    def initialize_pos(self):
        self.__cur_pos = self.__head.next

        if self.__cur_pos is None:
            return None

        return self.__cur_pos.item

    def next(self):
        if self.__cur_pos is None:
            return None

        self.__cur_pos = self.__cur_pos.next

        if self.__cur_pos is None:
            return None

        return self.__cur_pos.item

    def change_pair(self):
        prev = self.__head

        while prev.next is not None and prev.next.next is not None:
            next, curr = prev.next.next, prev.next
            next.next, curr.next, prev.next = curr, next.next, next
            if prev.next is not None:
                prev = prev.next.next
            else:
                break

    def swap_pairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swap_pairs(p.next)
            p.next = head

            return p

        return head

    def start_swap_pairs(self):
        self.__head.next = self.swap_pairs(self.__head.next)

    def odd_even_linked_list(self):
        if self.__head.next and self.__head.next.next and self.__head.next.next.next:
            odd_tail = self.__head.next
            even_head = self.__head.next.next
            even_tail = self.__head.next.next
            curr = self.__head.next.next.next

            index = 1

            while curr is not None:
                # 홀수번째이면
                if index % 2 == 1:
                    odd_tail.next = curr
                    odd_tail = curr
                    curr = curr.next
                    odd_tail.next = None
                else:
                    even_tail.next = curr
                    even_tail = curr
                    curr = curr.next
                    even_tail.next = None

                index += 1

            odd_tail.next = even_head


class LinkedListBasicIterator:
    def __init__(self, bList):
        self.__iterator = bList.getNodeOut(0)

    def __next__(self):
        if self.__iterator is None:
            raise StopIteration

        curItem = self.__iterator.item

        self.__iterator = self.__iterator.next

        return curItem
