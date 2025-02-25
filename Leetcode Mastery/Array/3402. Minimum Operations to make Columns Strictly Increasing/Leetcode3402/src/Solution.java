/*
 * Runtime: 1ms
 * Memory: 45.49MB
 */

public class Solution {
    public int minimumOperations(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int moves = 0;

        int i = 0;
        while (i < cols) {
            int j = 1;
            while (j < rows) {
                int prevCell = grid[j - 1][i];
                int currentCell = grid[j][i];
                if (currentCell <= prevCell) {
                    int newCellVal = prevCell + 1;
                    int diff = newCellVal - currentCell;
                    moves += diff;
                    grid[j][i] = newCellVal;
                }
                j++;
            }
            i++;
        }
        return moves;
    }   
}