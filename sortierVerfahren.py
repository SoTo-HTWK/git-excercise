def bubbleSort(array: []):
    #TODO fix user reported bug
    length = len(array)
    for i in range(0,length):
        for k in range(0,length-1):
            if array[i] > array[k]:
                array[i], array[k] = array[k], array[i]
    return array

def minSort(list:[]):
    length = len(list)
    if(length < 2):
        return list
    
    for i in range(0, length):
        minPos = findMinPos(i, list)
        list[i], list[minPos] = list[minPos], list[i]
    return list

def findMinPos(j: int, list:[]):
        pos = -1
    minVal = float('inf')
    for i in range (j, len(list)):
        if list[i]<minVal:
            minVal = list[i]
            pos = i
    return pos
