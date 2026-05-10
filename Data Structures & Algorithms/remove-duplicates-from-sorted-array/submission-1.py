class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 1, 1
        n =len(nums)-1

        while i<=n:
            if nums[i]!= nums[k-1]:
                nums[k] = nums[i]
                k+=1

            i+=1
        return k