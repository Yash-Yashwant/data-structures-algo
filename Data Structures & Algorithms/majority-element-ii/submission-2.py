class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ls = []
        Dic = {}

        for num in nums:
            Dic[num] = Dic.get(num, 0)+1
            # if Dic[num]>(len(nums)//3):
            #     if num not in ls:
            #         ls.append(num)
        # return ls
        return [num for num, count in Dic.items() if count > (len(nums)//3)]




