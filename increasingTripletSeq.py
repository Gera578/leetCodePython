
def getSecondMin(arr):
    if len(arr) < 2:
        return None
    
    first_min = min(arr)
    second_min = float('inf')
    for i in range(len(arr)):
        if arr[i] > first_min and arr[i] < second_min:
            second_min = arr[i]

    return second_min if second_min != float('inf') else None

def triplet(nums)-> bool:
    first_min = float('inf')
    second_min = float('inf')
    
    for num in nums:
        if num < first_min:  
            first_min = num  
        elif num > first_min and num < second_min:  
            second_min = num 
        elif num > second_min:  
            return True
    return False
             
    
    



print(getSecondMin(arr))
arr2 = [1,2,3,4,5]
print(triplet(arr2))