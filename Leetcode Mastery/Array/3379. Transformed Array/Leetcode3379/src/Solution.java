/*
 * Runtime: ms
 * Memory: MB
 */

public class Solution {
    public int[] constructTransformedArray(int[] nums) {
        if (nums.length == 1) {
            return nums;
        }
        
        int[] result = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                int index = i;
                int step = nums[i];
                if (index + step >= result.length) {
                    int diff = Math.abs(result.length - (index + step));
                    result[i] = nums[diff];
                } else {
                    result[i] = nums[index + step];
                } 
            } else if (nums[i] < 0) {
                int index = i;
                int step = Math.abs(nums[i]);
                if (index - step < 0) {
                    int toZero = i - 0;
                    int diff = step - toZero;
                    result[i] = nums[nums.length - diff]; 
                } else {
                    result[i] = nums[index - step];
                }
            } else {
                result[i] = nums[i];
            }
        }

        return result;
    }
}