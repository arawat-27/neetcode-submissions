# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list = []
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        while len(queue) > 0:
            level_list = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level_list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            list.append(level_list)

            level += 1
        return list