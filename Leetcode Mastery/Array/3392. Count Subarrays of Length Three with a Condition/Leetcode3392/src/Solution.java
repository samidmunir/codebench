/*
 * Runtime: 3ms
 * Memory: 45.28MB
 */

import java.util.Arrays;

public class Solution {
    public int countSubarrays(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length - 2; i++) {
            int[] subArray = Arrays.copyOfRange(nums, i, i + 3);
            if (isValidSubarray(subArray)) {
                count++;
            }
        }
        return count;
    }

    private boolean isValidSubarray(int[] arr) {
        boolean isValidSubarray = false;
        double sum = Double.valueOf(arr[0]) + Double.valueOf(arr[2]);
        double halfVal = Double.valueOf(arr[1]) / Double.valueOf(2);
        if (sum == halfVal) {
            isValidSubarray = true;
        }
        return isValidSubarray;
    }
}