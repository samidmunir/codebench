/*
 * Leetcode #3423
 *  Maximum Difference Between Adjaceent Elements in a Circular Array
 * 
 * Given a circular array nums, find the maximum absolute difference between adjacent elements.
 * 
 * Note: In a circular array, the first and last elements are adjacent.
 * 
 * Example 1:
 *  Input -> nums: [1, 2, 4]
 *  Output -> 3
 * 
 * Example 2:
 *  Input -> nums: [-5, -10, -5]
 *  Output -> 5
 */

 import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3423 -->");
        System.out.println("Maximum Difference Between Adjacent Elements in a Circular Array");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int[] nums1 = {1, 2, 4};
        int output1 = solution.maxAdjacentDistance(nums1);
        System.out.println("Test Case 1");
        System.out.println("nums: " + Arrays.toString(nums1));
        System.out.println("Output: " + output1 + "\n");

        // Test Case 2
        int[] nums2 = {-5, -10, -5};
        int output2 = solution.maxAdjacentDistance(nums2);
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.toString(nums2));
        System.out.println("Output: " + output2 + "\n");

        // Test Case 3
        int[] nums3 = {-4, -2, -3};
        int output3 = solution.maxAdjacentDistance(nums3);
        System.out.println("Test Case 3");
        System.out.println("nums: " + Arrays.toString(nums3));
        System.out.println("Output: " + output3 + "\n");
    }
}