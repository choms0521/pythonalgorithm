class ListStack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        return self.__stack.pop()

    def isEmpty(self) -> bool:
        if len(self.__stack) == 0:
            True
        else:
            False

    def top(self):
        if self.isEmpty():
            return self.__stack[len(self.__stack) - 1]
        else:
            return None

    def popAll(self):
        self.__stack = []
