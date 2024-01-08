# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lastTraversedNode = None
    change1 = None
    change2 = None

    def inOrderTraversal(self, node: Optional[TreeNode]):
        if node:
            self.inOrderTraversal(node.left)

            if self.lastTraversedNode:
                if self.lastTraversedNode.val >= node.val:
                    if not self.change1:
                        self.change1 = self.lastTraversedNode

                    self.change2 = node

            self.lastTraversedNode = node

            self.inOrderTraversal(node.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.inOrderTraversal(root)
        self.change1.val, self.change2.val = self.change2.val, self.change1.val
