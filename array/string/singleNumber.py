import operator
numbers = [2,2,1]

#time complexity = O(n) using xor
def singleNumberXor(numbers: list[int])->int:
    tr = 0
    for num in numbers:
        tr = operator.xor(tr, num)
        if tr is None:
            return 0
    return tr
print(singleNumberXor(numbers))

#time complexity = O(n^2) using count
def singleNumberCount(numbers: list[int])->int:
    for i in numbers:
        if numbers.count(i) == 1:
            continue
        return i

print(singleNumberCount(numbers))
        