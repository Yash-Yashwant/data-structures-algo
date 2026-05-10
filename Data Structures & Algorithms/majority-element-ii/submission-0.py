class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mDic = {}
        n = len(nums)
        mList = []
        majorElement = n//3

        for i in nums:
            mDic[i] = mDic.get(i, 0)+1

        for i in mDic:
            if mDic[i] > majorElement:
                mList.append(i)

        return mList

