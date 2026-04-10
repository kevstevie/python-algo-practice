# Problem: #104 - Maximum Depth of Binary Tree
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Submitted: 2026-04-06
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root, 0)


    def bfs(self, node, depth):
        if not node:
            return depth

        return max(self.bfs(node.left, depth + 1), \
        self.bfs(node.right, depth + 1))
