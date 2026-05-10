class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSet = set(nums)
        n = len(nums)
        longestSeq = 0

        for i in nums:
            if i-1 not in longestSet:
                num = i
                currentSeq = 1
                while (num+1) in  longestSet:
                    currentSeq += 1
                    num += 1
                longestSeq = max(longestSeq, currentSeq)

        return longestSeq



        






         
        