# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = list()

        if root:
            queue = list()
            queue.append(root)

            while queue:
                childNodes = list()
                currentLevelNodeValues = list()

                while queue:
                    node = queue.pop(0)
                    currentLevelNodeValues.append(node.val)

                    if node.left:
                        childNodes.append(node.left)
                    if node.right:
                        childNodes.append(node.right)

                if currentLevelNodeValues:
                    results.append(currentLevelNodeValues)

                while childNodes:
                    queue.append(childNodes.pop(0))
        
        return results   
