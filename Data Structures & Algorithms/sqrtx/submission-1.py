class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        if x == 0:
            return 0
        while l <= r:
            m = (l+r)//2

            if m**2 > x:
                r = m-1
            elif m**2 < x:
                l = m+1
            else: 
                return m

        return r


                 
        
  