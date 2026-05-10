class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # bs = [1:max(piles)]
        l, r = 1, max(piles)

        while l<=r:
            m = (l+r)//2
            total=0
            for pile in piles:
            
                total+=math.ceil(pile/m)
            if total<=h:
                res = m
                r = m-1

            else:
                l= m+1
        return res        