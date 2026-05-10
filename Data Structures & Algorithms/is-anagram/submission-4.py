class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1 = len(s)
        len2 = len(t)
        Dic1 = {}
        Dic2 = {}
        for i in range(len1):
            Dic1[s[i]] = Dic1.get(s[i], 0)+1
        for j in range(len2):
            Dic2[t[j]] = Dic2.get(t[j], 0)+1
        return Dic1 == Dic2
       


        
        