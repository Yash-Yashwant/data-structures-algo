class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        ls = []
        for i in range(min_len):
            ls.append(word1[i])
            ls.append(word2[i])
        ls.append(word1[min_len:])
        ls.append(word2[min_len:])

        return "".join(ls)


            
            
