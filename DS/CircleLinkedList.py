class ListNode:
    def __init__(self, newItem, nextNode: "ListNode"):
        self.item = newItem
        self.next = nextNode


# 141


class CircleLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__numItems = 0
        self.__tail.next = self.__tail

    def __getNode(self, i) -> ListNode:
        curr = self.__tail.next
        for index in range(i + 1):
            curr = curr.next

        return curr

    def getNode(self, i) -> ListNode:
        curr = self.__tail.next
        for index in range(i + 1):
            curr = curr.next

        return curr

    def insert(self, i: int, x):
        if i >= 0 and i < self.__numItems:
            prev = self.__getNode(i - 1)
            newNode = ListNode(x, prev.next)
            prev.next = newNode
            self.__numItems += 1
        # 마지막에 추가하는 거라면
        elif i == self.__numItems:
            self.append(x)
        else:
            print("outofboxerror")

    def append(self, x):
        temp = ListNode(x, self.__tail.next)
        self.__tail.next = temp
        self.__tail = temp

        self.__numItems += 1

    def __findNode(self, x) -> (ListNode, ListNode):
        prev = self.__tail.next
        curr = prev.next

        while curr != None:
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

        if i >= 0 and i < self.__numItems - 1:
            prev = self.__getNode(i - 1)
            curr = prev.next

            item = curr.item

            prev.next = curr.next
            self.__numItems -= 1

            return item

        elif i == self.__numItems - 1:
            prev = self.__getNode(i - 1)
            curr = prev.next
            item = curr.item
            prev.next = curr.next

            self.__tail = prev

            self.__numItems -= 1

            return item
        else:
            return None

    def remove(self, x):
        (prev, curr) = self.__findNode(x)

        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1

        if curr == self.__tail:
            self.__tail = prev

    def get(self, i):
        if self.isEmpty():
            return None

        if i >= 0 and i < self.__numItems:
            curr = self.__getNode(i)
            return curr.item
        else:
            return None

    def index(self, x):
        curr = self.__tail.next

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
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def count(self, x):
        curr = self.__tail.next

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
        copyList = CircleLinkedList()

        for index in range(self.__numItems):
            copyList.append(self.get(index))

        return copyList

    def reverse(self):
        __head = self.__tail.next
        prev = self.__tail.next
        curr = prev.next
        next = curr.next

        prev.next = self.__tail
        self.__tail = curr

        for i in range(self.__numItems):
            curr.next = prev
            prev = curr
            curr = next
            next = next.next

    def sort(self) -> None:
        a = []

        for index in range(self.__numItems):
            a.append(0, self.get(index))

        a.sort()

        self.clear()
        for index in range(len(a)):
            self.append(a[index])

    def printList(self) -> None:
        curr = self.__tail.next.next

        while curr != self.__tail.next:
            print(curr.item, end=" ")
            curr = curr.next

        print()

    def __iter__(self):
        return CirCularLinkedListIterator(self)

    def printInterval(self, i: int, j: int):
        startNode = self.__getNode(i)

        for index in range(0, j - i + 1):
            print(startNode.item)
            startNode = startNode.next

        print()


class CirCularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next

    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item
