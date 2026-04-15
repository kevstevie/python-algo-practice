# Problem: #2515 - Shortest Distance to Target String in a Circular Array
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
# Submitted: 2026-04-15
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        return min([min(abs(startIndex - i), abs(n - abs(startIndex - i))) for i in range(n) if words[i] == target], default=-1)

