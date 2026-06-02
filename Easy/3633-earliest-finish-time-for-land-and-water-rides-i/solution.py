# Problem: #3633 - Earliest Finish Time for Land and Water Rides I
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
# Submitted: 2026-06-02
# Tags: Array, Two Pointers, Binary Search, Greedy, Sorting
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        land_min = min(landStartTime[i] + landDuration[i] for i in range(n))
        water_min = min(waterStartTime[i] + waterDuration[i] for i in range(m))

        land_ans = min(max(land_min, waterStartTime[i]) + waterDuration[i] for i in range(m))
        water_ans = min(max(water_min, landStartTime[i]) + landDuration[i] for i in range(n))

        return min(land_ans, water_ans)
