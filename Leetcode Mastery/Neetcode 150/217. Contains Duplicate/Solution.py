from typing import List

"""
    Runtime: 10ms
    Memory: 35.02MB
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}
        for num in nums:
            if num not in numsMap:
                numsMap[num] = 1
            else:
                return True
        return False