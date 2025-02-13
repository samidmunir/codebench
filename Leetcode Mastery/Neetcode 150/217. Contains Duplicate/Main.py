"""
217. Contains Duplicate (Python3)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
    Input -> nums: [1, 2, 3, 1]
    Output -> true

Example 2:
    Input -> nums: [1, 2, 3, 4]
    Output -> false

Example 3:
    Input -> nums: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    Output -> true
"""

from Solution import Solution

def main():
    print('\n217. Contains Duplicate (Python3)\n')

    solution = Solution()

    # Test Case 1
    nums = [1, 2, 3, 1]
    output = solution.containsDuplicate(nums)
    print('Test Case 1')
    print(f'nums: {nums}')
    print(f'output: {output}\n')

    # Test Case 2
    nums = [1, 2, 3, 4]
    output = solution.containsDuplicate(nums)
    print('Test Case 2')
    print(f'nums: {nums}')
    print(f'output: {output}\n')

    # Test Case 3
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    output = solution.containsDuplicate(nums)
    print('Test Case 3')
    print(f'nums: {nums}')
    print(f'output: {output}\n')

if __name__ == '__main__':
    main()