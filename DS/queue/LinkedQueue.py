from DS.CircularDoublyLinkedList import *


class LinkedQueue:
    def __init__(self):
        self.__queue = CircularDoublyLinkedList()

    def enque(self, x):
        self.__queue.append(x)

    def deque(self):
        return self.__queue.pop(0)

    def front(self):
        return self.__queue.get(0)

    def isEmpty(self):
        return self.__queue.isEmpty()

    def dequeuAll(self):
        self.__queue = CircularDoublyLinkedList()

    def printQueue(self):
        self.__queue.printList()


# 2개의 큐를 사용하여 스텍의 push pop !!


class TemporalStack:
    def __init__(self):
        self.__firstQueue = LinkedQueue()
        self.__secondQueue = LinkedQueue()

    def push(self, x):
        self.__firstQueue.enque(x)

    def pop(self):
        lastValue = None
        while not self.__firstQueue.isEmpty():
            lastValue = self.__firstQueue.deque()

            if not self.__firstQueue.isEmpty():
                self.__secondQueue.enque(lastValue)

        if lastValue != None:
            tempQueue = self.__firstQueue
            self.__firstQueue = self.__secondQueue
            self.__secondQueue = tempQueue

        return lastValue
