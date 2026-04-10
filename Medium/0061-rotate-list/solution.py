# Problem: #61 - Rotate List
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/rotate-list/
# Submitted: 2026-04-06
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        l = []
        node = head
        while node:
            l.append(node)
            node = node.next
        
        l[-1].next = l[0]

        start = -k % len(l)
        l[start - 1].next = None

        return l[start]
        
