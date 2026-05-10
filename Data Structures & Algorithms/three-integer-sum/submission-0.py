class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        # i = 0
        n = len(nums) 
        # numsSort = nums.sort()
        nums.sort()
        for i in range(n) :
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low = i+1 
            high = n-1
    
            while low < high:
                currentSum = nums[i]+nums[low]+nums[high]
                if currentSum ==0:
                    arr.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low-1]:
                        low+=1
                    while low < high and nums[high] == nums[high+1]:
                        high-=1

                elif currentSum < 0:
                    low+=1
                else:
                    high-=1
        return arr
            # i +=1 
                


