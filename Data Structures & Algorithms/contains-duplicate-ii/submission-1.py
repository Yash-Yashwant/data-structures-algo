class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Dic ={}
        n = len(nums)

        for i in range(n):
            if nums[i] in Dic:
                absValue = abs(Dic[nums[i]] - i)
                if absValue <= k:
                    return True
                else:
                    Dic[nums[i]] = i
            else:
                Dic[nums[i]] = i
        return False
        