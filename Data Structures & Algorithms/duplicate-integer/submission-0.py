class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countDuplicate = {}
        for n in nums:
            if n not in countDuplicate:
                countDuplicate[n] = 1
            else:
                countDuplicate[n] += 1
        
        for n in countDuplicate:
            if countDuplicate[n] > 1:
                return True
        return False
        