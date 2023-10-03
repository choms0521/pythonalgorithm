from DS.heap.Heap import ListHeap


# n개의 원소에서 가장 큰 값을 찾아 맨뒤로 옮긴다.
# 그다음 큰 원소를 찾아 맨뒤 바로 앞에 놓는다.
# 마지막 자리까지 위 행위를 반복한다.


def selectSrot(list):
    for i in range(0, len(list)):
        maxIndex = 0
        for j in range(1, len(list) - i):
            if list[j] > list[maxIndex]:
                maxIndex = j

        tempValue = list[len(list) - i - 1]
        list[len(list) - i - 1] = list[maxIndex]
        list[maxIndex] = tempValue


def bubbleSort(list):
    for i in range(0, len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                tempValue = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tempValue


def insertSort(list):
    for i in range(1, len(list)):
        loc = i - 1

        newItem = list[i]

        while loc >= 0 and list[loc] > newItem:
            list[loc + 1] = list[loc]
            loc -= 1

        list[loc + 1] = newItem


def mergeSort(list, p: int, r: int):
    if p < r:
        q = (p + r) // 2
        mergeSort(list, p, q)
        mergeSort(list, q + 1, r)
        merge(list, p, q, r)


# 메모리에 약점이 있다, 메모리 이동 시간 낭비, 병합정렬
def merge(list, p: int, q: int, r: int):
    tempList = []
    leftIndex = p
    rightIndex = q + 1

    while leftIndex <= q and rightIndex <= r:
        if list[leftIndex] < list[rightIndex]:
            tempList.append(list[leftIndex])
            leftIndex += 1
        else:
            tempList.append(list[rightIndex])
            rightIndex += 1

    while leftIndex <= q:
        tempList.append(list[leftIndex])
        leftIndex += 1

    while rightIndex <= r:
        tempList.append(list[rightIndex])
        rightIndex += 1

    for i in range(0, len(tempList)):
        list[i + p] = tempList[i]


# 퀵정렬


def partition(list, p: int, r: int):
    x = list[r]

    insertIndex = p - 1
    for j in range(p, r):
        if list[j] < x:
            insertIndex += 1
            tempValue = list[j]
            list[j] = list[insertIndex]
            list[insertIndex] = tempValue

    insertIndex += 1
    tempValue = list[insertIndex]
    list[insertIndex] = list[r]
    list[r] = tempValue

    return insertIndex


def quickSort(list, p: int, r: int):
    if p < r:
        q = partition(list, p, r)
        quickSort(list, p, q - 1)
        quickSort(list, q + 1, r)


def heapSort(list):
    h = ListHeap(None)
    h.buildHeap(list)

    for i in range(len(list) - 1, -1, -1):
        value = h.deleteMax()
        list[i] = value
