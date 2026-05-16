class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mDic = {}

        for i in nums:
            mDic[i] = mDic.get(i,0)+1

        return max(mDic, key=mDic.get)