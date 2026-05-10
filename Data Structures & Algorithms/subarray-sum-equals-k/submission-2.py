class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Dic = {0:1}
        prefix = 0 
        count = 0 

        for i in nums:
            prefix += i
            check = (prefix-k)
            if check in Dic:
                count += Dic[check]

            Dic[prefix] = Dic.get(prefix, 0)+1
        return count 
            