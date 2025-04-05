class Solution:
    def stringCompresion(self, arr: list[str])->int:
        write = 0
        count= 1
        for i in range(len(arr)):
            char = arr[i] #the char will be eqaul to each char as we traverse the array
            if i+1 < len(arr) and arr[i] == arr[i+1]: #checks if the next char are equals and prevents go beyond limit
                count+=1 #increase + 1 if the next char and the previous are the same
            else:
                arr[write] = char # add to the array the char
                write+=1
                if count > 1: #if the count is less than 1, do not write the number
                    for digit in str(count):
                        arr[write] = digit # write the number as string in the array
                        write+=1 
                count = 1
        print(arr[:write])
        return write
arr = ["a","a","b","b","c","c","c","a","a"]
solution = Solution()
print(solution.stringCompresion(arr))