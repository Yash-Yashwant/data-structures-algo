class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dic = {}
        n = len(nums)
        majorityElement = n//2

        for i in range(n):
            Dic[nums[i]] = Dic.get(nums[i], 0) + 1

            if Dic[nums[i]] > majorityElement:
                return nums[i]


        