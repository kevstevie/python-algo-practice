/**
 * Problem: #1385 - Find the Distance Value Between Two Arrays
 * Difficulty: Easy
 * Language: Kotlin
 * URL: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
 * Submitted: 2026-11-05
 * Tags: Array, Two Pointers, Binary Search, Sorting
 */
class Solution {
    fun findTheDistanceValue(arr1: IntArray, arr2: IntArray, d: Int): Int {
        var ans = 0
        for (i in arr1) {
            var flag = true
            for (j in arr2) {
                if (abs(i - j) <= d) {
                    flag = false
                    break
                }
            }
            if (flag) {
                ans += 1
            }
        }
        return ans
    }
}
