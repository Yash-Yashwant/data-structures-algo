class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        L, R = 0, n-1

        while L < R:
            if s[L] != s[R]:
                subL, subR = s[L+1:R+1], s[L:R]
                return(subL==subL[::-1] or subR==subR[::-1])
         
            L, R = L+1, R-1

        return True

        