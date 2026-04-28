# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0
        self.dfs(root, float('-infinity'))
        return self.goodNodes

    def dfs(self, node, maxValue):
        if not node:
            return 

        if node.val >= maxValue:
            self.goodNodes += 1

        maxValue = max(maxValue, node.val)
        self.dfs(node.left, maxValue)
        self.dfs(node.right, maxValue)