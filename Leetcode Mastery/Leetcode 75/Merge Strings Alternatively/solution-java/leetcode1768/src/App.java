/*
 * Leetcode #1768 -> Merge Strings Alternatively
 * [Array/String]
 * 
 * You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional leters onto the end of the merged string.
 * 
 * Return the merged string.
 * 
 * Example 1)
 *  input: word1 = "abc", word2 = "pqr"
 *  output: apbqcr
 * 
 * Example 2)
 *  input: word1 = "ab", word2 = "pqrs", 
 *  output: apbqrs
 * 
 * Example 3)
 *  input: word1 = "abcd", word2 = "pq"
 *  output: apbqcd
 */

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Leetcode #1768 -->");
        System.out.println("Merge Strings Alternatively");
        System.out.println("-----------------------------------");

        Solution solution = new Solution();

        // Test Case 1
        String word1 = "abc";
        String word2 = "pqr";
        System.out.println("\nTest Case 1:");
        System.out.println("input -> word1: " + word1 + ", word2: " + word2);
        System.out.println("output -> " + solution.mergeAlternately(word1, word2));

        // Test Case 2
        word1 = "ab";
        word2 = "pqrs";
        System.out.println("\nTest Case 2:");
        System.out.println("input -> word1: " + word1 + ", word2: " + word2);
        System.out.println("output -> " + solution.mergeAlternately(word1, word2));

        // Test Case 3
        word1 = "abcd";
        word2 = "pq";
        System.out.println("\nTest Case 3:");
        System.out.println("input -> word1: " + word1 + ", word2: " + word2);
        System.out.println("output -> " + solution.mergeAlternately(word1, word2));
    }
}