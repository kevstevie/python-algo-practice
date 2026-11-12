/**
 * Problem: #3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
 * Difficulty: Easy
 * Language: Kotlin
 * URL: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
 * Submitted: 2026-11-12
 * Tags: Array
 */
class Solution {
    fun longestMonotonicSubarray(nums: IntArray): Int {
        var ans = 1
        var cur = nums[0]
        var temp = 1
        val n = nums.size

        for (i in 1..(n - 1)) {
            val now = nums[i]
            if (cur < now) {
                temp += 1
            } else {
                temp = 1
            }
            cur = now
            ans = max(ans, temp)
        }

        temp = 1
        cur = nums[0]

        for (i in 1..(n - 1)) {
            val now = nums[i]
            if (cur > now) {
                temp += 1
            } else {
                temp = 1
            }
            cur = now
            ans = max(ans, temp)
        }


        return ans
    }
}
