# Problem: #2418 - Sort the People
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/sort-the-people/
# Submitted: 2026-05-05
# Tags: Array, Hash Table, String, Sorting
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = [(names[i], heights[i]) for i in range(len(names))]

        l.sort(key=lambda x: -x[1])

        return [i[0] for i in l]
