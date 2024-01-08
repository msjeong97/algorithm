# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        self.result = False

        def dfs(node: Optional[TreeNode], currentSum: int):
            if node:
                if currentSum + node.val == targetSum and not node.left and not node.right:
                    self.result = True
                
                if not self.result:
                    dfs(node.left, currentSum + node.val)
                    dfs(node.right, currentSum + node.val)
        
        dfs(root, 0)

        return self.result
