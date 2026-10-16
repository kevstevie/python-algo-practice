/**
 * Problem: #3959 - Check Good Integer
 * Difficulty: Easy
 * Language: Java
 * URL: https://leetcode.com/problems/check-good-integer/
 * Submitted: 2026-10-16
 * Tags: Math, Simulation
 */
class Solution {
    public boolean checkGoodInteger(int n) {
        int digit = 0;
        int sq = 0;

        while (n > 0) {
            int cur = n % 10;
            digit += cur;
            sq += cur * cur;
            n /= 10;
        }
        if (sq - digit >= 50) {
            return true;
        }
        return false;
    }
}
