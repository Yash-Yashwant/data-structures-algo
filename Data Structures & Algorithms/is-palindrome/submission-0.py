class Solution:
    def isPalindrome(self, s: str) -> bool:
        palS = ""
        # there is white space issue  so have to remove the white space 
        lowercaseS = ""
        for char in s:
            if char.isalnum(): # we only need letter just for this question
                lowercaseS += char.lower() # lowercase              
        n = len(lowercaseS)
        i = n-1
        while i >=0:
            palS += lowercaseS[i]
            i -= 1
            
         
        if palS == lowercaseS:
            return True
        else:
            return False 
   
