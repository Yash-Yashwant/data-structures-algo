class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = len(strs)
        prefix = ''

        for char in range(len(strs[0])):
            for word in range(1, len(strs)):
               
                if char >= len(strs[word]):
                    return prefix
                if strs[word][char] != strs[0][char]:
                    return prefix

            prefix += strs[0][char]

        return prefix

    
        