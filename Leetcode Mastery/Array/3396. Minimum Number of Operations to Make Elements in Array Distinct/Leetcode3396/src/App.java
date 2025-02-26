/*
 * Leetcode #3396
 *  Minimum Number of Operations to Make Elements in Array Distinct
 * 
 * You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
 * - Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
 * 
 * Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.
 * 
 * Example 1:
 *  Input --> nums: [1, 2, 3, 4, 2, 3, 3, 5, 7]
 *  Output --> 2
 * 
 * Example 2:
 *  Input --> nums: [4, 5, 6, 4, 4]
 *  Output --> 2
 * 
 * Example 3:
 *  Input --> nums: [6, 7, 8, 9]
 *  Output --> 0
 */

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3396 -->");
        System.out.println("Minimum Number of Operations to Make Elements in Array Distinct");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        int nums1[] = {1, 2, 3, 4, 2, 3, 3, 5, 7};
        int output1 = solution.minimumOperations(nums1);
        System.out.println("Test Case 1");
        System.out.println("nums: " + Arrays.toString(nums1));
        System.out.println("output: " + output1 + "\n");

        // Test Case 2
        int nums2[] = {4, 5, 6, 4, 4};
        int output2 = solution.minimumOperations(nums2);
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.toString(nums2));
        System.out.println("output: " + output2 + "\n");

        // Test Case 3
        int nums3[] = {6, 7, 8, 9};
        int output3 = solution.minimumOperations(nums3);
        System.out.println("Test Case 3");
        System.out.println("nums: " + Arrays.toString(nums3));
        System.out.println("output: " + output3 + "\n");
    }
}