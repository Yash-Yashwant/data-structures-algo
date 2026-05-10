class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        j = 0 
        i = n - 1

        while j < i:
            s[j], s[i] = s[i], s[j]
            i -=1 
            j += 1
        