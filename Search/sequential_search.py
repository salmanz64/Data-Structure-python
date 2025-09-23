

from typing import List


def search(nums:List[dict],key:int):
    found = False
    
    i=0
    while i<len(nums) and not found:
        if nums[i]==key:
            found = True
        else:
            i+=1
    return i

print(search([1,2,6,3,3,33,11,57],33))