class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        value = 0
        windowSize = float('inf') # because im getting min vlaue and if set to 0 that is going to min always as all the values are positive

        for r in range(n):
            value += nums[r]
            if value >= target:
                while value >= target:
                    windowSize = min(windowSize, (r-l)+1)
                    value-=nums[l]
                    l+=1

        return windowSize if windowSize != float('inf') else 0 
        # this is condition is important because if no window exists, 
        #then it will return inf which we dont dont want isntead should return 0

