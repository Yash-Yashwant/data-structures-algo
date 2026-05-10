class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        lsDic = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            lsDic[key].append(word)

        return list(lsDic.values())