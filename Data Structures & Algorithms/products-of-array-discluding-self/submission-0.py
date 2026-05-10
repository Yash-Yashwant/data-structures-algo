class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1 
        post = 1 
        n = len(nums)
        output = [0] * n

        for i in range(n):
            output[i] = pre
            pre *= nums[i]
        
        for j in range(n-1, -1, -1):
            output[j] *= post
            post *= nums[j]

        return output



        