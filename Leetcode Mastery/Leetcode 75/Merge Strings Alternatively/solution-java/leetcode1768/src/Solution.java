/*
 * Runtime: 6ms
 * Memory: 43.05 MB
 */
public class Solution {
    public String mergeAlternately(String word1, String word2) {
        String mergedString = "";

        int word1Length = word1.length();
        int word2Length = word2.length();

        if (word1Length < word2Length) {
            int pointer = 0;
            while (pointer < word1Length) {
                mergedString += word1.charAt(pointer);
                mergedString += word2.charAt(pointer);
                pointer++;
            }
            mergedString += word2.substring(pointer, word2Length);
        } else if (word1Length > word2Length) {
            int pointer = 0;
            while (pointer < word2.length()) {
                mergedString += word1.charAt(pointer);
                mergedString += word2.charAt(pointer);
                pointer++;
            }
            mergedString += word1.substring(pointer, word1Length);
        } else {
            for (int i = 0; i < word1Length; i++) {
                mergedString += word1.charAt(i);
                mergedString += word2.charAt(i);
            }
        }

        return mergedString;
    }
}