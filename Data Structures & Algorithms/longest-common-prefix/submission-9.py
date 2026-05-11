class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest=[]

        for i in range(len(min(strs, key=len))):
            for s in strs[1:]:
                if s[i]!=strs[0][i]:
                    return ''.join(longest)
            longest.append(strs[0][i])
        return ''.join(longest)