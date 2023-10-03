# 힙의 조건
# 완전 이진 트리
# 노드 값이 자식 노드 값보다 크거나 같다.


class ListHeap:
    def __init__(self, list=None):
        if list is None:
            self.__heapArr = []
        else:
            self.__heapArr = list

            parentIndex = (len(self.__heapArr) - 1) // 2

            while parentIndex >= 0:
                self.__percolateDown(parentIndex)
                parentIndex -= 1

    def __makeHeap(self, i: int):
        parentIndex = i

        if parentIndex >= 0:
            leftIndex = 2 * parentIndex + 1
            rIndex = 2 * parentIndex + 2

            if leftIndex <= len(self.__heapArr) - 1:
                if self.__heapArr[leftIndex] > self.__heapArr[parentIndex]:
                    tempValue = self.__heapArr[parentIndex]
                    self.__heapArr[parentIndex] = self.__heapArr[leftIndex]
                    self.__heapArr[leftIndex] = tempValue
                    self.__makeHeap(leftIndex)

                if rIndex <= len(self.__heapArr) - 1:
                    if self.__heapArr[rIndex] > self.__heapArr[parentIndex]:
                        tempValue = self.__heapArr[parentIndex]
                        self.__heapArr[parentIndex] = self.__heapArr[rIndex]
                        self.__heapArr[rIndex] = tempValue
                        self.__makeHeap(rIndex)

    def insert(self, x):
        childIndex = len(self.__heapArr)
        self.__heapArr.append(x)

        parentIndex = (childIndex - 1) // 2
        while parentIndex >= 0:
            parentValue = self.__heapArr[parentIndex]

            if parentValue < x:
                self.__heapArr[parentIndex] = x
                self.__heapArr[childIndex] = parentValue

                childIndex = parentIndex
                parentIndex = (childIndex - 1) // 2
            else:
                break

    def __percolateDown(self, i: int) -> None:
        child = 2 * i + 1
        right = 2 * i + 2
        heapLength = len(self.__heapArr)

        if child <= heapLength - 1:
            if (
                right <= heapLength - 1
                and self.__heapArr[child] < self.__heapArr[right]
            ):
                child = right

            if self.__heapArr[i] < self.__heapArr[child]:
                tempValue = self.__heapArr[i]
                self.__heapArr[i] = self.__heapArr[child]
                self.__heapArr[child] = tempValue
                self.__percolateDown(child)

    def deleteMax(self):
        if self.isEmpty():
            return None

        bigValue = self.__heapArr[0]
        self.__heapArr[0] = self.__heapArr[len(self.__heapArr) - 1]
        self.__heapArr.pop()
        self.__percolateDown(0)

        return bigValue

    def isEmpty(self):
        return len(self.__heapArr) == 0

    def max(self):
        return self.__heapArr[0]

    def clear(self):
        self.__heapArr = []

    def buildHeap(self, list):
        for i in range(0, len(list)):
            self.insert(list[i])
