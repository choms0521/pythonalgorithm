class BidirectNode:
    def __init__(self, x, prevNode: "BidirectNode", nextNode: "BidirectNode"):
        self.prev = prevNode
        self.next = nextNode
        self.item = x


class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.next = self.__head
        self.__head.prev = self.__head
        self.__numOfItems = 0

    def getNode(self, index: int):
        if index > self.__numOfItems:
            return None

        curr = self.__head
        for i in range(0, index + 1):
            curr = curr.next

        return curr

    def insert(self, i: int, newItem) -> None:
        if i >= 0 and i <= self.__numOfItems:
            prevNode = self.getNode(i - 1)
            nextNode = prevNode.next

            newNode = BidirectNode(newItem, prevNode, nextNode)

            prevNode.next = newNode
            nextNode.prev = newNode
            self.__numOfItems += 1
        else:
            print("something wrong", i, "outof list")

    def append(self, newItem) -> None:
        lastNode = self.__head.prev
        newNode = BidirectNode(newItem, lastNode, self.__head)
        lastNode.next = newNode
        self.__head.prev = newNode
        self.__numOfItems += 1

    def isEmpty(self):
        if self.__numOfItems == 0:
            return True

        return False

    def pop(self, *args) -> BidirectNode:
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numOfItems - 1

        if i >= 0 and i <= self.__numOfItems - 1:
            currNode = self.getNode(i)
            curItem = currNode.item
            prevNode = currNode.prev
            nextNode = currNode.next

            prevNode.next = nextNode
            nextNode.prev = prevNode

            self.__numOfItems -= 1

            return curItem
        else:
            return None

    def __findNode(self, x):
        if self.__numOfItems == 0:
            return None

        curr = self.__head
        for i in range(0, self.__numOfItems):
            curr = curr.next
            if curr.item == x:
                return curr

        return None

    def remove(self, x):
        curr = self.__findNode(x)

        if curr == None:
            return None

        curr.prev.next = curr.next
        curr.next.preve = curr.prev

        self.__numOfItems -= 1
        return x

    def get(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numOfItems - 1

        if i >= 0 and i <= self.__numOfItems - 1:
            currNode = self.getNode(i)

            return currNode.item
        else:
            return None

    def index(self, x):
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1

        return -1

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)

    def size(self):
        return self.__numOfItems

    def clear(self):
        self.__head.next = self.__head
        self.__head.prev = self.__head
        self.__numOfItems = 0

    def count(self, x) -> int:
        cnt = 0

        for element in self:
            if element == x:
                cnt += 1

        return cnt

    def extend(self, a):
        for element in a:
            self.append(a)

    def copy(self) -> "CircularDoublyLinkedList":
        newList = CircularDoublyLinkedList()

        for element in self:
            newList.append(element)

        return newList

    def reverse(self):
        curr = self.__head
        nextNode = curr.next
        for i in range(0, self.__numOfItems):
            curr = nextNode
            nextNode = curr.next
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp

        firstNode = self.__head.next
        self.__head.next = self.__head.prev
        self.__head.prev = firstNode

    def printList(self):
        for element in self:
            print(element)

        print()

    def contains(self, x) -> bool:
        index = self.index(x)

        if index > 0:
            return True

        return False

    def add(self, x) -> None:
        curr = self.__head

        while curr.next != self.__head:
            curr = curr.next

            if x < curr.item:
                prev = curr.prev
                newNode = BidirectNode(x, prev, curr)
                prev.next = newNode
                curr.prev = newNode
                self.__numOfItems = 0
                return

        self.append(x)


class CircularDoublyLinkedListIterator:
    def __init__(self, cList):
        self.__iterator = cList.getNode(0)

    def __next__(self):
        if self.__iterator.item == "dummy":
            raise StopIteration

        curValue = self.__iterator.item
        self.__iterator = self.__iterator.next

        return curValue
