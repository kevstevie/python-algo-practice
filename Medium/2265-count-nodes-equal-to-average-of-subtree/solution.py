# Problem: #2265 - Count Nodes Equal to Average of Subtree
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
# Submitted: 2026-09-10
# Tags: Tree, Depth-First Search, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def recur(node):
            nonlocal ans
            if node == None:
                return [0, 0]
            left = recur(node.left)
            right = recur(node.right)
            val = left[0] + right[0] + node.val
            cnt = left[1] + right[1] + 1
            if val // cnt == node.val:
                ans += 1
            
            return [val, cnt]
        
        recur(root)
        
        return ans
