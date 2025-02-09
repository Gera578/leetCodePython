count = []

def isVowel(s):
    vowels = 'aeiouAEIOU'
    for char in s:
        if char in vowels:
            return True
            
    return False

def reverseVowels(string):
    i, j =0, len(string)-1# two pointers. 1 starts at 0, j at the end of the string
    string = list(string) # convert the string into a list to easy access 
    vowel = 'aeiouAEIOU' # set the vowels
    
    while i < j:  # Loop until the two pointers meet
        if string[i] in vowel and string[j] in vowel:  # If both characters at i and j are vowels
            string[i], string[j] = string[j], string[i]  # Swap the vowels
            i += 1  # Move the start pointer to the right
            j -= 1  # Move the end pointer to the left
        if string[i] not in vowel:  # If the character at i is not a vowel
            i += 1  # Move the start pointer to the right
        if string[j] not in vowel:  # If the character at j is not a vowel
            j -= 1  # Move the end pointer to the left
    
    # for i in range(len(string)):
            
    #     if isVowel(string[i]):
    #         vowels[j] = string[i]
    #         j+=1
    
    # for i in range(len(string)):
    #     if isVowel(string[i]):
    #         j-=1
    #         string[i] = vowels[j]
    return ''.join(string)

s = 'hello'
print(s)

print(reverseVowels(s))
    