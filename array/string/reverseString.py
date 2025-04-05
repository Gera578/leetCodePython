def reverseString(s):
   words = s.split()
   
   reversed_words = ""
   
   for word in reversed(words):
        reversed_words +=word + " "
       
   return reversed_words.strip()
    
    
s = "a good example"
print(reverseString(s))
   
