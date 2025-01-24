
class Palindrome:
    def isPalindrome(self, x: int) -> bool:
        str_x= str(x)
        
        reversed_str_x = str_x[::-1]
        
        return str_x == reversed_str_x

class PalindromeInt:
    def isPalindromeInt(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        
        original_x = x
        reversed_int = 0
        while x > 0:
            digit = x % 10
            reversed_int = reversed_int * 10 + digit
            x //= 10
            
        return original_x == reversed_int
checkerInt = PalindromeInt()
number = 1221

print(checkerInt.isPalindromeInt(number))


