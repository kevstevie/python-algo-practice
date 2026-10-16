/**
 * Problem: #1480 - Running Sum of 1d Array
 * Difficulty: Easy
 * Language: Java
 * URL: https://leetcode.com/problems/running-sum-of-1d-array/
 * Submitted: 2026-10-16
 * Tags: Array, Prefix Sum
 */
class Solution {
    public int[] runningSum(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
        }
        for (int i = 1; i < n; i++) {
            ans[i] += ans[i - 1];
        }
        
        return ans;
    }
}
