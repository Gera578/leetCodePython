

str1 = 'abcabcabc'
str2 = 'abc'

def gcd(str1, str2):
    while str2:
        str1,str2 = str2, str1% str2
    return str1

n = gcd(len(str1), len(str2))
print(str2[:n])
