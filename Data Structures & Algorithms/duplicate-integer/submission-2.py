class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Ill use set to check becuase set only has unqiue

        unique = set()

        for i in nums:
            if i in unique:
                return True
            unique.add(i)
        return False

        
        