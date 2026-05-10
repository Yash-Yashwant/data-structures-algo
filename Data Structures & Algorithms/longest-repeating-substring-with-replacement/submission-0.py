class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestSub = 0 
        Dic = {}
        l, r = 0, 0

        for r in range(len(s)):

            # if r in Dic:
            #     Dic[s[r]]+=1
            # else:
            #     Dic[s[r]] = 1
            # the above and below both are same
            Dic[s[r]] = Dic.get(s[r], 0)+1
            maxFreq = max(Dic.values())
            windowSize = (r-l)+1
            while windowSize-maxFreq > k:
                Dic[s[l]]-=1
                l+=1
                windowSize = (r-l)+1
            longestSub = max(longestSub, windowSize)
        return longestSub



                

            

        

        