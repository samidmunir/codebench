/*
 * Runtime: 1ms
 * Memory: 41.82MB
 */

public class Solution {
    public int countPartitions(int[] nums) {
        int count = 0;
        int partitionIndex = 0;
        int firstSum = 0;
        int secondSum = 0;

        while (partitionIndex < nums.length - 1) {
            firstSum = 0;
            for (int i = 0; i <= partitionIndex; i++) {
                firstSum += nums[i];
            }
            secondSum = 0;
            for (int j = partitionIndex + 1; j < nums.length; j++) {
                secondSum += nums[j];
            }
            int absDifference = Math.abs(firstSum - secondSum);
            if (absDifference % 2 == 0) {
                count++;
            }
            partitionIndex++;
        }

        return count;
    }
}