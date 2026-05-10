class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stackArr = []

        for i in range(n):
            if s[i] in '([{':
                stackArr.append(s[i])
            else:
                if not stackArr:
                    return False
                else:
                    char = s[i]
                    top = stackArr.pop()
                    if char == ')' and top != '(':
                        return False
                    if char == '}' and top != '{':
                        return False
                    if char == ']' and top != '[':
                        return False

        return len(stackArr) == 0

