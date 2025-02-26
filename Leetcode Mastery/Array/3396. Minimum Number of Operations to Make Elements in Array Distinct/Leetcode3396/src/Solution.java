/*
 * Runtime: 5ms
 * Memory: 44.29MB
 */

import java.util.HashSet;
import java.util.Arrays;

public class Solution {
    public int minimumOperations(int[] nums) {
        if (nums.length == 0 || nums.length == 1) {
            return 0;
        }

        int[] arr = nums.clone();
        int operationCount = 0;

        while (containsDuplicate(arr)) {
            if (arr.length <= 3) {
                operationCount++;
                break;
            } else {
                arr = Arrays.copyOfRange(arr, 3, arr.length);
                operationCount++;
            }
        }

        return operationCount;
    }

    private boolean containsDuplicate(int[] arr) {
        if (arr.length == 0 || arr.length == 1) {
            return false;
        }

        HashSet<Integer> arrSet = new HashSet<>();
        int i = 0;
        int n = arr.length;
        while (i < n) {
            if (arrSet.contains(arr[i])) {
                return true;
            } else {
                arrSet.add(arr[i]);
            }
            i++;
        }

        return false;
    }
}