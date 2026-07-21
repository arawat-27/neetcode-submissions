class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for i in nums:
            if i == 0:
                res = max(res, cnt)
                cnt = 0
            else:
                cnt +=1
        return max(cnt, res)