/*
 * Runtime: 929ms
 * Memory: 44.92MB
 */

import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    public int maxLength(int[] nums) {
        int n = nums.length;
        int maxLength = 0;
        int currentLength = 0;

        int i = 0;

        while (i < n - 1) {
            int j = i + 1;
            while (j < n) {
                int[] subArray = Arrays.copyOfRange(nums, i, j + 1);
                int product = product(subArray);
                int gcd = gcd(subArray);
                int lcm = lcm(subArray);
                if (lcm * gcd == product) {
                    currentLength = subArray.length;
                    maxLength = Math.max(maxLength, currentLength);
                }
                j++;
            }
            i++;
        }

        return maxLength;
    }

    private int product(int[] arr) {
        int product = 1;

        for (int i = 0; i < arr.length; i++) {
            product *= arr[i];
        }

        return product;
    }

    private int gcd(int[] arr) {
        int gcd = 1;
        ArrayList<Integer> cds = new ArrayList<>();

        int i = gcd;
        int j = 0;
        while (i <= 10) {
            j = 0;
            while (j < arr.length) {
                if (arr[j] % i == 0) {
                    j++;
                } else {
                    break;
                }
            }
            if (j == arr.length) {
                cds.add(i);
            }
            i++;
        }

        Object[] cdsArr = cds.toArray();
        gcd = (int) cdsArr[cdsArr.length - 1];

        return gcd;
    }

    private int lcm(int[] arr) {
        int n = arr.length;
        boolean flag = false;
        Arrays.sort(arr);
        int lcm = arr[n - 1];

        while (!flag) {
            int i = 0;
            while (i < n) {
                if (lcm % arr[i] == 0) {
                    i++;
                } else {
                    break;
                }
            }
            if (i >= n) {
                flag = true;
            } else {
                lcm += arr[n - 1];
            }
        }

        return lcm;
    }
}