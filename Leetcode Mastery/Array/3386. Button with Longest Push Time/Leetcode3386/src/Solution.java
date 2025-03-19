import java.util.HashMap;

public class Solution {
    public int buttonWithLongestTime(int[][] events) {
        int n = events.length;
        int buttonWithLongestTime = 0;
        int maxTime = Integer.MIN_VALUE;

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            if (!map.containsKey(events[i][0])) {
                map.put(events[i][0], events[i][1]);
            } else {
                
            }
        }

        return buttonWithLongestTime;
    }
}