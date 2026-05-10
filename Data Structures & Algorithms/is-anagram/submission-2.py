class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        string1 = {}
        string2 = {}

        for i in s:

            # if i in string1:
            string1[i] = string1.get(i, 0) + 1

            

        for j in t:
            # if i in string2:
            string2[j] = string2.get(j, 0) + 1
            # else:
            #     string2.add(i)
        
        if string1 == string2:
            return True

        else:
            return False