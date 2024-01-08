# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = list()

        def inOrderTraversal(node: Optional[TreeNode]):
            if node:
                inOrderTraversal(node.left)
                result.append(node.val)
                inOrderTraversal(node.right)

        inOrderTraversal(root)

        for i in range(0, len(result) - 1):
            if result[i] >= result[i + 1]:
                return False

        return True
