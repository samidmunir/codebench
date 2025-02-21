/*
 * Leetcode #3417
 *  Zigzag Grid Traversal with Skip
 * 
 * You are given a m x n 2D array grid of positive integers.
 * 
 * Your task is to traverse grid in a zigzag pattern while skipping every alternate cell.
 * 
 * Zigzag pattern is defined as following the below actions:
 * - Start the top-left cell (0, 0)
 * - Move right within a row until the end of the row is reached.
 * - Drop down to the next row, then traverse left until the beginning of the row is reached.
 * - Continue alternating between right and left traveral until every row has been traversed.
 * 
 * Note that you must skip every alterante cell during the traversal.
 * 
 * Return the array of integers result containing, in order, the value of the cells visited during the zigzag traversal with skips.
 * 
 * Example 1:
 *  Input --> grid: [[1, 2], [3, 4]]
 *  Output --> [1, 4]
 * 
 * Example 2:
 *  Input --> grid: [[2, 1], [2, 1], [2, 1]]
 *  Output --> [2, 1, 2]
 * 
 * Example 3:
 *  Input --> grid: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 *  Output --> [1, 3, 5, 7, 9]
 */

import java.util.Arrays;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3417 -->");
        System.out.println("Zigzag Grid Traversal with Skip");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int[][] grid1 = {{1, 2}, {3, 4}};
        List<Integer> output1 = solution.zigzagTraversal(grid1);
        System.out.println("Test Case 1");
        System.out.println("grid: " + Arrays.deepToString(grid1));
        System.out.println("Output: " + output1 + "\n");

        // Test Case 2
        int[][] grid2 = {{2, 1}, {2, 1}, {2, 1}};
        List<Integer> output2 = solution.zigzagTraversal(grid2);
        System.out.println("Test Case 2");
        System.out.println("grid: " + Arrays.deepToString(grid2));
        System.out.println("Output: " + output2 + "\n");

        // Test Case 3
        int[][] grid3 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        List<Integer> output3 = solution.zigzagTraversal(grid3);
        System.out.println("Test Case 3");
        System.out.println("grid: " + Arrays.deepToString(grid3));
        System.out.println("Output: " + output3 + "\n");

        // Test Case 4
        int[][] grid4 = {{1, 2, 1, 3}, {5, 15, 7, 3}, {10, 4, 14, 12}};
        List<Integer> output4 = solution.zigzagTraversal(grid4);
        System.out.println("Test Case 4");
        System.out.println("grid: " + Arrays.deepToString(grid4));
        System.out.println("Output: " + output4 + "\n");
    }
}