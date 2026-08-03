# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #go through each level and check if there is more than one element
        #if there is more than one element, only output the outmost right element
        #print only elements with one element in each level
        res = []
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()
                if i == level_length - 1:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return res