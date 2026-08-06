class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countLettersInS = {}
        countLettersInT = {}

        for n in s:
            if n not in countLettersInS:
                countLettersInS[n] = 1
            else:
                countLettersInS[n] += 1

        for n in t:
            if n not in countLettersInT:
                countLettersInT[n] = 1
            else:
                countLettersInT[n] += 1
        
        if countLettersInS == countLettersInT:
            return True
        else:
            return False


        