"""
238. Product of Array Except Itself

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffic of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input -> nums = [1, 2, 3, 4]
    Output -> [24, 12, 8, 6]

Example 2:
    Input -> nums = [-1, 1, 0, -3, 3]
    Output -> [0, 0, 9, 0, 0]
"""

from Solution import Solution

def main():
    print('\n238. Product of Array Except Itself (Python3)\n')

    solution = Solution()

    # Test Case 1
    nums = [1, 2, 3, 4]
    output = solution.productExceptItself(nums = nums)
    print('Test Case 1')
    print(f'nums: {nums}')
    print(f'output: {output}\n')

    # Test Case 2
    nums = [-1, 1, 0, -3, 3]
    output = solution.productExceptItself(nums = nums)
    print('Test Case 1')
    print(f'nums: {nums}')
    print(f'output: {output}\n')

if __name__ == '__main__':
    main()