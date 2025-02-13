"""
1. Two Sum

Given an array of integer nums and an integer target, return indices of the two number such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input -> nums: [2, 7, 11, 15], target = 9
    Output -> [0, 1]

Example 2:
    Input -> nums: [3, 2, 4], target = 6
    Output -> [1, 2]

Example 3:
    Input -> nums: [3, 3], target = 6
    Output -> [0, 1]
"""

from Solution import Solution

def main():
    print('\n1. Two Sum (Python3)\n')

    solution = Solution()

    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    output = solution.twoSum(nums = nums, target = target)
    print('Test Case 1')
    print(f'nums: {nums}')
    print(f'target: {target}')
    print(f'output: {output}\n')

    # Test Case 2
    nums = [3, 2, 4]
    target = 6
    output = solution.twoSum(nums = nums, target = target)
    print('Test Case 1')
    print(f'nums: {nums}')
    print(f'target: {target}')
    print(f'output: {output}\n')

    # Test Case 3
    nums = [3, 3]
    target = 6
    output = solution.twoSum(nums = nums, target = target)
    print('Test Case 1')
    print(f'nums: {nums}')
    print(f'target: {target}')
    print(f'output: {output}\n')

if __name__ == '__main__':
    main()