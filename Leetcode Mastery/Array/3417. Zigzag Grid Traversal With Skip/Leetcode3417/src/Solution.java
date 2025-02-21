/*
 * Runtime: 1ms
 * Memory: 45.60MB
 */

import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<Integer> zigzagTraversal(int[][] grid) {
        List<Integer> result = new ArrayList<Integer>();
        int i = 0;
        int j = 0;

        int rows = grid.length;
        int cols = grid[0].length;

        if (cols % 2 == 0) {
            while (i < rows) {
                if (i % 2 == 0) {
                    j = 0;
                    while (j < cols) {
                        result.add(grid[i][j]);
                        j += 2;
                    }
                } else {
                    j = cols - 1;
                    while (j >= 0) {
                        result.add(grid[i][j]);
                        j -= 2;
                    }
                }
                i++;
            }
        } else {
            while (i < rows) {
                if (i % 2 == 0) {
                    j = 0;
                    while (j < cols) {
                        result.add(grid[i][j]);
                        j += 2;
                    }
                } else {
                    j = cols - 2;
                    while (j >= 0) {
                        result.add(grid[i][j]);
                        j -= 2;
                    }
                }
                i++;
            }
        }

        return result;
    }
}