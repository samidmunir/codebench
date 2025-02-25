/*
 * Leetcode #3392
 *  Count Subarrays of Length Three with a Condition
 * 
 * Given an integer array nums, return the number of subarrays of length three such that the sum of the first and third numbers equals exactly half of the second number.
 * 
 * Example 1:
 *  Input --> nums: [1, 2, 1, 4, 1]
 *  Output --> 1
 * 
 * Example 2:
 *  Input --> nums: [1, 1, 1]
 *  Output --> 0
 */

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3392 -->");
        System.out.println("Count Subarrays of Length Three with a Condition");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int nums1[] = {1, 2, 1, 4, 1};
        int output1 = solution.countSubarrays(nums1);
        System.out.println("Test Case 1");
        System.out.println("nums: " + Arrays.toString(nums1));
        System.out.println("output: " + output1 + "\n");

        // Test Case 2
        int nums2[] = {1, 1, 1};
        int output2 = solution.countSubarrays(nums2);
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.toString(nums2));
        System.out.println("output: " + output2 + "\n");

        // Test Case 3
        int nums3[] = {-1, -4, -1, 4};
        int output3 = solution.countSubarrays(nums3);
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.toString(nums3));
        System.out.println("output: " + output3 + "\n");
    }
}