class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list = []
        for num in nums:
            if num == val:
                continue
            new_list.append(num)
        for i in range(len(new_list)):
                nums[i] = new_list[i]
        return len(new_list)
        

        
        