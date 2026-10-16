/**
 * Problem: #1232 - Check If It Is a Straight Line
 * Difficulty: Easy
 * Language: Java
 * URL: https://leetcode.com/problems/check-if-it-is-a-straight-line/
 * Submitted: 2026-10-16
 * Tags: Array, Math, Geometry
 */
class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        double sub = (double) (coordinates[0][1] - coordinates[1][1])/ (coordinates[0][0] - coordinates[1][0]);
        boolean flag = false;
        if (coordinates[0][0] - coordinates[1][0] == 0) {
            flag = true;
        }

        int n = coordinates.length;

        for (int i = 1; i < n; i++) {
            double temp = (double) (coordinates[i][1] - coordinates[i - 1][1])/ (coordinates[i][0] - coordinates[i - 1][0]);

            if (flag) {
                if (coordinates[i][0] - coordinates[i - 1][0] != 0) {
                    return false;
                }
            } else {
                if (sub != temp) {
                    return false;
                }
            }
        }
        
        return true;
    }
}
