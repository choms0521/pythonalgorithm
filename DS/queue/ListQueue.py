class ListQueue:
    def __init__(self):
        self.__queue = []

    def enque(self, x):
        self.__queue.append(x)

    def deque(self):
        if len(self.__queue) > 0:
            return self.__queue.pop(0)

        return None

    def front(self):
        if len(self.__queue) > 0:
            return self.__queue[0]

        return None

    def isEmpty(self):
        return len(self.__queue) == 0

    def dequeuAll(self):
        self.__queue = []

    def printQueue(self):
        for i in range(0, len(self.__queue)):
            print(self.__queue[i])

        print()
