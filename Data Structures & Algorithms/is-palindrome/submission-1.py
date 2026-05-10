class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        for ch in s:
            if ch.isalnum():
                ls.append(ch.lower())
        sString = "".join(ls)
        return sString == sString[::-1]