/*
 * Leetcode #3379
 *  Transformed Array
 * 
 * You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:
 * 
 * For each index i (where 0 <= i < nums.length), perform the following independent actions:
 * - If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
 * - If nums[i] < 0: Start an index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
 * - If nums[i] == 0: Set result[i] to nums[i].
 * 
 * Return the new array result.
 * 
 * Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.
 * 
 * Example 1:
 *  Input --> nums: [3, -2, 1, 1]
 *  Output --> [1, 1, 1, 3]
 * 
 * Example 2:
 *  Input --> nums: [-1, 4, -1]
 *  Output --> [-1, -1, 4]
 */

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3379 -->");
        System.out.println("Transformed Array");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int[] nums1 = {3, -2, 1, 1};
        int[] output1 = solution.constructTransformedArray(nums1);
        System.out.println("Test Case 1");
        System.out.println("nums[]: " + Arrays.toString(nums1));
        System.out.println("output: " + Arrays.toString(output1) + "\n");

        // Test Case 2
        int[] nums2 = {-1, 4, -1};
        int[] output2 = solution.constructTransformedArray(nums2);
        System.out.println("Test Case 1");
        System.out.println("nums[]: " + Arrays.toString(nums2));
        System.out.println("output: " + Arrays.toString(output2) + "\n");

        // // Test Case 3
        int[] nums3 = {-10};
        int[] output3 = solution.constructTransformedArray(nums3);
        System.out.println("Test Case 3");
        System.out.println("nums[]: " + Arrays.toString(nums3));
        System.out.println("output: " + Arrays.toString(output3) + "\n");

        // Test Case 4
        int[] nums4 = {5, -3, 2, 1};
        int[] output4 = solution.constructTransformedArray(nums4);
        System.out.println("Test Case 4");
        System.out.println("nums[]: " + Arrays.toString(nums4));
        System.out.println("output: " + Arrays.toString(output4) + "\n");
    }
}