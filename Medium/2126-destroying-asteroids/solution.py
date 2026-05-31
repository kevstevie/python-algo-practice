# Problem: #2126 - Destroying Asteroids
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/destroying-asteroids/
# Submitted: 2026-05-31
# Tags: Array, Greedy, Sorting
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        cur = mass

        asteroids.sort()

        for i in asteroids:
            if cur < i:
                return False
            cur += i
        
        return True

