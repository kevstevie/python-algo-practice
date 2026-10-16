/**
 * Problem: #476 - Number Complement
 * Difficulty: Easy
 * Language: Java
 * URL: https://leetcode.com/problems/number-complement/
 * Submitted: 2026-10-16
 * Tags: Bit Manipulation
 */
class Solution {
    public int findComplement(int num) {
        long cur = 1;
        while (cur <= num) {
            cur *= 2;
        }
        return (int) (cur - (long) num - 1L);
    }
}
