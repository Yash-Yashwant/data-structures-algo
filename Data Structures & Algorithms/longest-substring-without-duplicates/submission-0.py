class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        stringSet = set()
        n = len(s)
        maxStringLen = 0

        for r in range(n):
            while s[r] in stringSet:
                stringSet.remove(s[l])
                l +=1
            stringSet.add(s[r])
            maxStringLen = max(maxStringLen, (r-l)+1)
        return maxStringLen
            
        