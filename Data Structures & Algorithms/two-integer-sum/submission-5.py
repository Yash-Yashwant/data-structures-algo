class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, w in enumerate(nums):
            diff = target-w
            if diff in dic:
                return [dic[diff], i]
            dic[w] = i


