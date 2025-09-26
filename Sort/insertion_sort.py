from typing import List


def insertionSort(arr:List[int])->List[int]:
    for index in range(1,len(arr)):
        currentValue = arr[index]
        position = index
        
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position = position -1
            
        arr[position] = currentValue
        

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

            