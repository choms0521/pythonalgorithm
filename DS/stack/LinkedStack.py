from DS.LinkedList import *


class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()

    def push(self, x):
        self.__list.insert(0, x)

    def pop(self):
        return self.__list.pop(0, 1)

    def isEmpty(self) -> bool:
        return self.__list.isEmpty()

    def top(self):
        if self.isEmpty():
            return None
        return self.__list.get(0)

    def popAll(self):
        self.__list.clear()

    def copy(self):
        newStack = LinkedStack()
        tempStack = LinkedStack()

        for element in self.__list:
            tempStack.push(element)

        while tempStack.isEmpty() == False:
            newStack.push(tempStack.pop())

        return newStack


def isOperator(ch):
    return ch == "+" or ch == "-" or ch == "/" or ch == "*"


def operation(opr2: int, opr1: int, operator: str) -> int:
    return {"+": opr1 + opr2, "-": opr1 - opr2, "*": opr1 * opr2, "/": opr1 // opr2}[
        operator
    ]


def evaluate(p):
    s = LinkedStack()

    digitPreviously = False
    for i in range(len(p)):
        ch = p[i]

        if ch.isdigit():
            if digitPreviously:
                curNum = s.pop()
                s.push(curNum * 10 + int(ch))

            else:
                s.push(int(ch))
                digitPreviously = True

        elif isOperator(ch):
            num1 = s.pop()
            num2 = s.pop()
            result = operation(num1, num2, ch)
            s.push(result)
            digitPreviously = False
        else:
            digitPreviously = False

    return s.pop()


def parenBalance(s: str) -> bool:
    firstStack = LinkedStack()
    secondStack = LinkedStack()

    for i in range(len(s)):
        if s[i] == "(":
            firstStack.push()


def checkNum3Problem(wStr: str) -> bool:
    s = LinkedStack()
    insertStack = True
    isSuccessStr = True
    for i in range(0, len(wStr)):
        if wStr[i] == "$":
            insertStack = False
            continue

        if insertStack:
            s.push(wStr[i])

        else:
            if wStr[i] != s.pop():
                isSuccessStr = False
                break

    return isSuccessStr
