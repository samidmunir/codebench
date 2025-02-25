/*
 * Leetcode #3411
 *  Maximum Subarray With Equal Products
 * 
 * You are given an array of positive integers nums.
 * 
 * An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
 * - prod(arr) is the product of all elements of arr.
 * - gcd(arr) is the GCD of all elements of arr.
 * - lcm(arr) is the LCM of all elements of arr.
 * 
 * Return the length of the longest product equivalent subarry of nums.
 * 
 * Example 1:
 *  Input --> nums: [1, 2, 1, 2, 1, 1, 1]
 *  Output --> 5
 * 
 * Example 2:
 *  Input --> nums: [2, 3, 4, 5, 6]
 *  Output --> 3
 * 
 * Example 3:
 *  Input --> nums: [1, 2, 3, 1, 4, 5, 1]
 *  Output --> 5
 */

 import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3411 -->");
        System.out.println("Maximum Subarray With Equal Products");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int[] nums1 = {1, 2, 1, 2, 1, 1, 1};
        int output1 = solution.maxLength(nums1);
        System.out.println("Test Case 1");
        System.out.println("nums: " + Arrays.toString(nums1));
        System.out.println("output: " + output1 + "\n");

        // Test Case 2
        int[] nums2 = {2, 3, 4, 5, 6};
        int output2 = solution.maxLength(nums2);
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.toString(nums2));
        System.out.println("output: " + output2 + "\n");

        // Test Case 3
        int[] nums3 = {1, 2, 3, 1, 4, 5, 1};
        int output3 = solution.maxLength(nums3);
        System.out.println("Test Case 3");
        System.out.println("nums: " + Arrays.toString(nums3));
        System.out.println("output: " + output3 + "\n");

        // Test Case 4
        int[] nums4 = {3, 6, 12, 42};
        int output4 = solution.maxLength(nums4);
        System.out.println("Test Case 3");
        System.out.println("nums: " + Arrays.toString(nums4));
        System.out.println("output: " + output4 + "\n");
    }
}