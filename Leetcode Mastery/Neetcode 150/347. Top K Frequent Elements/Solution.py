from typing import List

"""
    Runtime: 2938ms
    Memory: 21.03MB
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        print(f'nums: {nums}')

        numsMap = {}
        for num in nums:
            if num not in numsMap:
                numsMap[num] = 1
            else:
                numsMap[num] += 1

        print(f'numsMap: {numsMap}')

        seen = {}
        counts = []
        for num in nums:
            if num not in seen:
                seen[num] = 1
                counts.append(numsMap[num])
        counts.sort(reverse = True)
        print(f'counts: {counts}')

        result = []

        counts = counts[:k]

        seen = {}

        for count in counts:
            print(f'count: {count}')
            for num in nums:
                if num not in seen and numsMap[num] == count:
                    seen[num] = 1
                    result.append(num)

        return result