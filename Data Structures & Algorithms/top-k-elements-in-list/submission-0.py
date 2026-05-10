class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        kDic = {}

        bucket =[[] for i in range(len(nums)+1)]

        for i in nums:
            kDic[i] = kDic.get(i, 0) + 1

        
        for key in kDic:
            bucket[kDic.get(key)].append(key)

        result =[]
        for i in range(-1, -len(bucket)-1, -1 ):
            for j in bucket[i]:
                result.append(j)

                if len(result) == k:
                    return result

        

        





