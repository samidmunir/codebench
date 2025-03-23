/*
 * Runtime: 3 ms
 * Memory: 45.4 MB
 */

import java.util.HashMap;

public class Solution {
    public int buttonWithLongestTime(int[][] events) {
        int n = events.length;

        if (n == 1) {
            return events[0][0];
        }

        HashMap<Integer, Integer> bTimeMap = new HashMap<>();

        int maxPressTime = events[0][1];
        int buttonWithLongestPressTime = events[0][0];

        for (int i = 0; i < n; i++) {
            int buttonID = events[i][0];
            int buttonPressDuration;
            if (i == 0) {
                buttonPressDuration = events[i][1];
            } else {
                buttonPressDuration = events[i][1] - events[i - 1][1];
            }

            if (!bTimeMap.containsKey(buttonID)) {
                bTimeMap.put(buttonID, buttonPressDuration);
                if (buttonPressDuration > maxPressTime) {
                    maxPressTime = Math.max(maxPressTime, buttonPressDuration);
                }
            } else {
                int lastButtonPressDuration = bTimeMap.get(buttonID);
                if (buttonPressDuration >= lastButtonPressDuration) {
                    bTimeMap.put(buttonID, buttonPressDuration);
                    maxPressTime = Math.max(maxPressTime, buttonPressDuration);
                }
            }
        }

        int smallestButtonIndex = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int buttonID = events[i][0];
            int buttonPressDuration = bTimeMap.get(buttonID);
            if (buttonPressDuration == maxPressTime) {
                smallestButtonIndex = Math.min(smallestButtonIndex, buttonID);
            }
        }

        buttonWithLongestPressTime = smallestButtonIndex;

        return buttonWithLongestPressTime;
    }
}