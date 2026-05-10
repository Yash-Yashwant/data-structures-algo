class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Dic = {}
        for i in range(len(nums)):
           
            if nums[i] in Dic:
                if abs(Dic[nums[i]] - i) <= k:
                    return True
            
            Dic[nums[i]] = i
            

        return False