from typing import List

"""
    Runtime: 0ms
    Memory: 19.12MB
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i in range(len(nums)):
            if nums[i] not in numsMap:
                numsMap[nums[i]] = i    
            complement = target - nums[i]
            if complement in numsMap and numsMap[complement] != i:
                return [numsMap[complement], i]
