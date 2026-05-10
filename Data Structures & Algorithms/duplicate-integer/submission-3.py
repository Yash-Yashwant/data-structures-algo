class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setDuplicate = set()
        n = len(nums)

        for i in range(n):
            if nums[i] in setDuplicate:
                return True
            setDuplicate.add(nums[i])
        return False
