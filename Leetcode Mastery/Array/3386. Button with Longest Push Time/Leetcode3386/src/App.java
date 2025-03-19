/*
 * Leetcode #3386 ->
 *  Button with Longest Push Time
 * 
 * You are given a 2D arary events with represents a sequence of events where a child pushes a series of buttons on a keyboard.
 * 
 * Each events[i] = [index(i), time(i)] indicates that the button at index(i) was pressed at time(i).
 * - The array is sorted in increasing order of time.
 * - The time taken to press a button is the difference in time between consecutive button presses. The time for the first button is simply the time at which it was pressed.
 * 
 * Return the index of the button that took the longest time to push. If multiple buttons have the same longest time, return the button with the smallest index.
 * 
 * Example 1)
 *  Input -> nums: [[1, 2], [2, 5], [3, 9], [1, 15]]
 *  Output -> 1
 * 
 * Example 2)
 *  Input -> nums: [[10, 5], [1, 7]]
 *  Output -> 10
 */

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #3386 -->");
        System.out.println("Button with Longest Push Time");
        System.out.println("-----------------------------------\n");

        Solution solution = new Solution();

        // Test Case 1
        int[][] nums1 = {{1, 2}, {2, 5}, {3, 9}, {1, 15}};
        System.out.println("Test Case 1");
        System.out.println("nums: " + Arrays.deepToString(nums1));
        System.out.println("output: " + solution.buttonWithLongestTime(nums1) + "\n");

        // Test Case 2
        int[][] nums2 = {{10, 5}, {1, 7}};
        System.out.println("Test Case 2");
        System.out.println("nums: " + Arrays.deepToString(nums2));
        System.out.println("output: " + solution.buttonWithLongestTime(nums2) + "\n");
    }
}