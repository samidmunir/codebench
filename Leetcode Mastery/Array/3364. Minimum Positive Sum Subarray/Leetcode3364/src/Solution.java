import java.util.List;

public class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int n = nums.size();
        int minSum = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int count = l;
            while (count <= r) {
                if (i + count > n) {
                    break;
                }
                int currentSum = 0;
                for (int j = i; j < i + count; j++) {
                    currentSum += nums.get(j);
                }
                if (currentSum > 0) {
                    minSum = Math.min(minSum, currentSum);
                }
                count++;
            }
        }

        if (minSum == Integer.MAX_VALUE) {
            return -1;
        } else {
            return minSum;
        }
    }
}