class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valueSet = set()
        for i in nums:
            if i in valueSet:
                return True
            valueSet.add(i)
        return False