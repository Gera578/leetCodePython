def productArrayExceotSelf(num: list) -> list:
    left = 1
    right = 1
    
    
    answer = [1] * len(num)
    for i in range(len(num)):
        answer[i] = left
        left *= num[i]
    
    for i in range(len(num) -1, -1, -1):
        answer[i]*=right
        right*= num[i]
    return answer
    
arr = [1,2,3,4]
print(arr)

print(productArrayExceotSelf(arr))