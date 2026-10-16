/**
 * Problem: #1502 - Can Make Arithmetic Progression From Sequence
 * Difficulty: Easy
 * Language: Java
 * URL: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
 * Submitted: 2026-10-16
 * Tags: Array, Sorting
 */
class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        long sub = arr[1] - arr[0];

        for (int i = 2; i < n; i++) {
            long temp = arr[i] - arr[i - 1];
            if (temp != sub) {
                return false;
            }
        }
        return true;
    }
}
