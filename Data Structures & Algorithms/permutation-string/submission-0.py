class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        lenS2 = len(s2)
        Dic1 = {}

        for char1 in range(lenS1):
            Dic1[s1[char1]] = Dic1.get(s1[char1], 0)+1
        
        for char2 in range((lenS2-lenS1)+1):
            # if s2[char2: char2+lenS1] == Dic1:
            #     return True. # i need have this as a dictionary to compare
            # string cannot be compared to. dictionary
            windowDic = {}
            window = s2[char2: char2+lenS1]
            for char in window:
                windowDic[char] = windowDic.get(char, 0)+1
            if windowDic == Dic1:
                return True
        return False



