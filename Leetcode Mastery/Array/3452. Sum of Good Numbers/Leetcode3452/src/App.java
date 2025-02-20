/*
 * Leetcode #3452
 *  Sum of Good Numbers
 * 
 * Given an array of integer nums and an integer k, an element nums[i] is considered good if it strictly greater than the elements at indices i - k and i + k (if those indices exist). If neither of those indices exists, nums[i] is still considered good.
 * 
 * Return the sum of all good elements in the array.
 * 
 * Example 1:
 *  Input --> nums: [1, 3, 2, 1, 5, 4], k: 2
 *  Output --> 12
 * 
 * Example 2:
 *  Input --> nums: [2, 1], k: 1
 *  Output --> 2
 */

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3452 -->");
        System.out.println("Sum of Good Numbers");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int[] nums1 = {1, 3, 2, 1, 5, 4};
        int k1 = 2;
        int output1 = solution.sumOfGoodNumbers(nums1, k1);
        System.out.println("Test Case 1");
        System.out.println("nums: " + Arrays.toString(nums1));
        System.out.println("k: " + k1);
        System.out.println("Output: " + output1 + "\n");

        // Test Case 2
        int[] nums2 = {2, 1};
        int k2 = 1;
        int output2 = solution.sumOfGoodNumbers(nums2, k2);
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.toString(nums2));
        System.out.println("k: " + k2);
        System.out.println("Output: " + output2 + "\n");
    }
}