class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for i in nums:
            if i in unique:
                return True
            else:
                unique.add(i)
        # check every element and if no True then we come out of loop and print false
        return False
        