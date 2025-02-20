/*
 * Runtime: 1ms
 * Memory: 43.63MB
 */

public class Solution {
    public int subarraySum(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        if (nums.length == 1) {
            return nums[0];
        }

        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            int start = Math.max(0, i - nums[i]);
            int currentSum = 0;
            for (int j = start; j <= i; j++) {
                currentSum += nums[j];
            }
            sum += currentSum;
        }

        return sum;
    }
}