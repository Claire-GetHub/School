from math import ceil

def linearSearch(list, target):

    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def binarySearch1(list, target):
    i = ceil(len(list)/2)
    if i > len(list) - 1 or i < len(list) - 1:
        return -1
    elif list[i] == target:
        return i
    elif list[i] > target:
        return binarySearch1(list[:i], target)
    elif list[i] < target:
        return binarySearch1(list[i:], target)


def binarySearch2(list, target):
    temp = list[:]
    i = 0
    while list[i] != target:
        i = ceil(len(list)/2)
        if i > len(temp) - 1 or i < len(temp) - 1:
            return -1
        if list[i] > target:
            temp = temp[:i]
        elif list[i] < target:
            temp = temp[i:]
    return i


print(binarySearch2([1,2,3], 3))