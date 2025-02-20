/*
 * Runtime: 1ms
 * Memory: 43.33MB
 */

public class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int maxDiff = 0;
        int currentDiff = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i == nums.length - 1) {
                currentDiff = Math.abs(nums[i] - nums[0]);
            } else {
                currentDiff = Math.abs(nums[i] - nums[i + 1]);
            }
            maxDiff = Math.max(maxDiff, currentDiff);
        }

        return maxDiff;
    }
}