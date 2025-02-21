/*
 * Leetcode #3432
 *  Count Partitions with Even Sum Difference
 * 
 * You are given an integer array nums of length n.
 * 
 * A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:
 * - Left subarray contains indices [0, i].
 * - Right subarray contains indices [i + 1, n - 1].
 * 
 * Return the number of partitions where the difference between the sum of the left and right subarrays is even.
 * 
 * Example 1:
 *  Input --> nums: [10, 10, 3, 7, 6]
 *  Output --> 4
 * 
 * Example 2:
 *  Input --> nums: [1, 2, 2]
 *  Output --> 0
 * 
 * Example 3:
 *  Input --> nums: [2, 4, 6, 8]
 *  Output --> 3
 */

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3432 -->");
        System.out.println("Count Partitions with Even Sum Difference");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int[] nums1 = {10, 10, 3, 7, 6};
        int output1 = solution.countPartitions(nums1);
        System.out.println("Test Case 1");
        System.out.println("nums: " + Arrays.toString(nums1));
        System.out.println("Output: " + output1 + "\n");

        // Test Case 2
        int[] nums2 = {1, 2, 2};
        int output2 = solution.countPartitions(nums2);
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.toString(nums2));
        System.out.println("Output: " + output2 + "\n");

        // Test Case 3
        int[] nums3 = {2, 4, 6, 8};
        int output3 = solution.countPartitions(nums3);
        System.out.println("Test Case 3");
        System.out.println("nums: " + Arrays.toString(nums3));
        System.out.println("Output: " + output3 + "\n");
    }
}