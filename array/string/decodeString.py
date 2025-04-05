
digit = ""
stack = []
temp = ""
group = []
s = "3[a2[c]]"

for i in s:
    if i.isdigit():
        digit += i
    elif i == "[":
        stack.append((temp, int(digit) if digit else 1))
        temp = ""
        digit = ""
    elif i == "]":
        prev, num = stack.pop()
        temp = prev + temp * num
    else:
        temp += i
print(temp)

