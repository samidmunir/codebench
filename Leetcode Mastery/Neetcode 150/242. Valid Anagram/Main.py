"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
    Input -> s = "anagram", t = "nagaram"
    Output -> true

Example 2:
    Input -> s = "rat", t = "car"
    Output -> false
"""

from Solution import Solution

def main():
    print('\n242. Valid Anagram (Python3)\n')

    solution = Solution()

    # Test Case 1
    s = "anagram"
    t = "nagaram"
    output = solution.isAnagram(s = s, t = t)
    print('Test Case 1')
    print(f's: {s}, t: {t}')
    print(f'output: {output}\n')

    # Test Case 2
    s = "rat"
    t = "car"
    output = solution.isAnagram(s = s, t = t)
    print('Test Case 2')
    print(f's: {s}, t: {t}')
    print(f'output: {output}\n')

if __name__ == '__main__':
    main()