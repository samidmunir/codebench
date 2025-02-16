"""
347. Top K Frequent Elements

Example 1:
    Input -> nums = [], k = 2
    Output -> [1, 2]

Example 2:
    Input -> nums = [], k = 2
    Output = [1]
"""

from Solution import Solution

def main():
    print('\n347. Top K Frequent Elements (Python3)\n')

    solution = Solution()
    
    # Test Case 1
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    output = solution.topKFrequent(nums = nums, k = k)
    print('Test Case 1')
    print(f'nums: {nums}, k: {k}')
    print(f'output: {output}\n')

    # Test Case 2
    nums = [1]
    k = 1
    output = solution.topKFrequent(nums = nums, k = k)
    print('Test Case 2')
    print(f'nums: {nums}, k: {k}')
    print(f'output: {output}\n')

    # Test Case 3
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    k = 3
    output = solution.topKFrequent(nums = nums, k = k)
    print('Test Case 3')
    print(f'nums: {nums}, k: {k}')
    print(f'output: {output}\n')

    # Test Case 4
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    k = 10
    output = solution.topKFrequent(nums = nums, k = k)
    print('Test Case 4')
    print(f'nums: {nums}, k: {k}')
    print(f'output: {output}\n')

if __name__ == '__main__':
    main()