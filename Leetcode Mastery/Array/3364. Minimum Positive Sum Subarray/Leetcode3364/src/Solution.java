import java.util.List;

public class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int minSum = Integer.MAX_VALUE;
        int left = 0;
        int right = left + 1;

        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                
            }
        }

        if (minSum < 0) {
            return -1;
        } else {
            return minSum;
        }
    }
}