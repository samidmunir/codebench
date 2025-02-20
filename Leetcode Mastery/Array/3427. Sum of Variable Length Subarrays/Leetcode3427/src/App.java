/*
 * Leetcode #3427
 *  Sum of Variable Length Subarrays
 * 
 * You are given an integer array nums of size n. For each index i where 0 <= i < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).
 * 
 * Return the total sum of all elements from the subarray defined for each index in the array.
 * 
 * Example 1:
 *  Input --> nums: [2, 3, 1]
 *  Output --> 11
 * 
 * Example 2:
 *  Input --> nums: [3, 1, 1, 2]
 *  Output --> 13
 */

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3427 -->");
        System.out.println("Sum of Variable Length Subarrays");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int[] nums1 = {2, 3, 1};
        int output1 = solution.subarraySum(nums1);
        System.out.println("Test Case 1");
        System.out.println("nums: " + Arrays.toString(nums1));
        System.out.println("Output: " + output1 + "\n");

        // Test Case 2
        int[] nums2 = {3, 1, 1, 2};
        int output2 = solution.subarraySum(nums2);
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.toString(nums2));
        System.out.println("Output: " + output2 + "\n");

        // Test Case 3
        // int[] nums3 = {-4, -2, -3};
        // int output3 = solution.subarraySum(nums3);
        // System.out.println("Test Case 3");
        // System.out.println("nums: " + Arrays.toString(nums3));
        // System.out.println("Output: " + output3 + "\n");
    }
}