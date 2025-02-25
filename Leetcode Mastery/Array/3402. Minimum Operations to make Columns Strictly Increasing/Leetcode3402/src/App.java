/*
 * Leetcode #3402
 *  Minimum Operations to make Columns Strictly Increasing
 * 
 * You are given a m x n matrix grid of non-negative integers.
 * 
 * In one operation, you can increment the value of any grid[i][j] by 1.
 * 
 * Return the minimum number of operations needed to make all columns of grid strictly increasing.
 * 
 * Example 1:
 *  Input --> grid: [[3, 2], [1, 3], [3, 4], [0, 1]]
 *  Output --> 15
 * 
 * Example 2:
 *  Input --> grid: [[3, 2, 1], [2, 1, 0], [1, 2, 3]]
 *  Output --> 12
 */

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3402 --> ");
        System.out.println("Minimum Operations to make Columns Strictly Increasing");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int[][] grid1 = {{3, 2}, {1, 3}, {3, 4}, {0, 1}};
        int output1 = solution.minimumOperations(grid1);
        System.out.println("Test Case 1");
        System.out.println("grid[][]: " + Arrays.deepToString(grid1));
        System.out.println("output: " + output1 + "\n");

        // Test Case 2
        int[][] grid2 = {{3, 2, 1}, {2, 1, 0}, {1, 2, 3}};
        int output2 = solution.minimumOperations(grid2);
        System.out.println("Test Case 1");
        System.out.println("grid[][]: " + Arrays.deepToString(grid2));
        System.out.println("output: " + output2 + "\n");
    }
}