/*
 * Runtime: 1ms
 * Memory: 44.80MB
 */

public class Solution {
    public int[] constructTransformedArray(int[] nums) {
        if (nums.length == 1) {
            return nums;
        }

        int n = nums.length;
        int[] result = new int[n];

        int i = 0;
        while (i < nums.length) {
            if (nums[i] > 0) {
                int currentIndex = i;
                int step = nums[i];
                int newIndexToBe = currentIndex + step;
                if (newIndexToBe >= n) {
                    int count = 0;
                    int index = i;
                    while (count < step) {
                        if (index >= n - 1) {
                            index = 0;
                        } else {
                            index++;
                        }
                        count++;
                    }
                    result[i] = nums[index];
                } else {
                    result[i] = nums[newIndexToBe];
                }
            } else if (nums[i] < 0) {
                int currentIndex = i;
                int step = Math.abs(nums[i]);
                int newIndexToBe = currentIndex - step;
                if (newIndexToBe < 0) {
                    int count = 0;
                    int index = i;
                    while (count < step) {
                        if (index <= 0) {
                            index = n - 1;
                        } else {
                            index--;
                        }
                        count++;
                    }
                    result[i] = nums[index];
                } else {
                    result[i] = nums[newIndexToBe];
                }
            } else {
                result[i] = nums[i];
            }
            i++;
        }
        
        return result;
    }
}