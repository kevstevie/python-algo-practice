# Problem: #23 - Merge k Sorted Lists
# Difficulty: Hard
# Language: Python3
# URL: https://leetcode.com/problems/merge-k-sorted-lists/
# Submitted: 2026-04-10
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def devide(l):
            if len(l) == 1:
                return l[0]
            mid = len(l) // 2
            left = devide(l[:mid])
            right = devide(l[mid:])
            return merge(left, right)

        def merge(left, right):
            root = ListNode()
            cur = root
            l = left
            r = right
            while l and r:
                if l.val <= r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            while l:
                cur.next = l
                l = l.next
                cur = cur.next
            while r:
                cur.next = r
                r = r.next
                cur = cur.next

            return root.next

        if not lists:
            return None
        return devide(lists)
