/*
 * Leetcode #3364
 *  Minimum Positive Sum Subarray
 * 
 * You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.
 * 
 * Return minimum sum of such a subarray. If no such subarray exists, return -1.
 * 
 * A subarray is a contiguous non-empty sequence of elements within an array.
 * 
 * Example 1:
 *  Input --> nums: [3, -2, 1, 4], l = 2, r = 3
 *  Output --> 1
 * 
 * Example 2:
 *  Input --> nums: [-2, 2, -3, 1], l = 2, r = 3
 *  Output --> -1
 * 
 * Example 3:
 *  Input --> nums: [1, 2, 3, 4], l = 2, r = 4
 */

import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode 3364 -->");
        System.out.println("Minimum Positive Sum Subarray");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        List<Integer> nums1 = new ArrayList<>();
        nums1.add(3);
        nums1.add(-2);
        nums1.add(1);
        nums1.add(4);
        int l1 = 2;
        int r1 = 3;
        int output1 = solution.minimumSumSubarray(nums1, l1, r1);
        System.out.println("Test Case 1 -->");
        System.out.println("nums<>: " + nums1.toString());
        System.out.println("\tl: " + l1);
        System.out.println("\tr: " + r1);
        System.out.println("output: " + output1 + "\n");

        // Test Case 2
        List<Integer> nums2 = new ArrayList<>();
        nums2.add(-2);
        nums2.add(2);
        nums2.add(-3);
        nums2.add(1);
        int l2 = 2;
        int r2 = 3;
        int output2 = solution.minimumSumSubarray(nums2, l2, r2);
        System.out.println("Test Case 2 -->");
        System.out.println("nums<>: " + nums2.toString());
        System.out.println("\tl: " + l2);
        System.out.println("\tr: " + r2);
        System.out.println("output: " + output2 + "\n");

        // Test Case 3
        List<Integer> nums3 = new ArrayList<>();
        nums3.add(1);
        nums3.add(2);
        nums3.add(3);
        nums3.add(4);
        int l3 = 2;
        int r3 = 4;
        int output3 = solution.minimumSumSubarray(nums3, l3, r3);
        System.out.println("Test Case 3 -->");
        System.out.println("nums<>: " + nums3.toString());
        System.out.println("\tl: " + l3);
        System.out.println("\tr: " + r3);
        System.out.println("output: " + output3 + "\n");   
    }
}