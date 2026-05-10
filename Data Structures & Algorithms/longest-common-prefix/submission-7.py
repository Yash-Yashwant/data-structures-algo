class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        ls = []

        for i in range(n):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i]!=strs[j][i]:
                    return "" .join(ls) 
            ls.append(strs[0][i])

        return "".join(ls)
