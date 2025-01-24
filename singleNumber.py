import operator
numbers = [2,2,1]

#time complexity = O(n) using xor
tr = 0
for num in numbers:
    tr = operator.xor(tr, num)
print(tr)

#time complexity = O(n^2) using count
for i in numbers:
    if numbers.count(i) == 1:
        print(i)