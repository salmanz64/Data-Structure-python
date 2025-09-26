from typing import List


def selectionSort(arr:List[int])->List[int]:
    for fillslot in range(len(arr)-1,0,-1):
        positionMax = 0
        for location in range(1,fillslot+1):
            if arr[location]>arr[positionMax]:
                positionMax = location
        temp = arr[fillslot]
        arr[fillslot]=arr[positionMax]
        arr[positionMax] = temp
        
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
                    
    