"""
49. Group Anagram

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
    Input -> strs: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output -> [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Example 2:
    Input -> strs: [""]
    Output -> [[""]]

Example 3:
    Input -> strs: ["a"]
    Output -> [["a"]]
"""

from Solution import Solution

def main():
    print('\n49. Group Anagrams (Python3)\n')

    solution = Solution()

    # Test Case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = solution.groupAnagrams(strs = strs)
    print('Test Case 1')
    print(f'strs: {strs}')
    print(f'output: {output}\n')

    # Test Case 2
    strs = [""]
    output = solution.groupAnagrams(strs = strs)
    print('Test Case 2')
    print(f'strs: {strs}')
    print(f'output: {output}\n')

    # Test Case 3
    strs = ["a"]
    output = solution.groupAnagrams(strs = strs)
    print('Test Case 3')
    print(f'strs: {strs}')
    print(f'output: {output}\n')

if __name__ == '__main__':
    main()