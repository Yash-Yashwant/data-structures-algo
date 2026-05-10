class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        eSet = set(nums)
        maxStreak = 0
        

        for num in eSet:
            if (num-1) not in eSet:
                curr = num
                currStreak = 1 
                while(curr+1) in eSet:
                    currStreak+=1
                    curr+=1
                maxStreak = max(currStreak, maxStreak)

        return maxStreak

        

       