class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        emptyS=[]
        n1, n2 = len(word1), len(word2)
        max_len = max(n1, n2)
        while i < max_len:
            if i < n1:
                emptyS.append(word1[i])
            if i < n2:
                emptyS.append(word2[i])
            i+=1
        return ''.join(emptyS)