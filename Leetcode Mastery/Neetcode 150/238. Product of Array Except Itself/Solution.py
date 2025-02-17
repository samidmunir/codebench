from typing import List

"""
    Runtime: ms
    Memory: MB
"""

class Solution:
    def productExceptItself(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        answer = []

        lastProduct = 1
        for i in range(len(nums)):
            if i == 0:
                prefix = 1 * nums[i]
                lastProduct = prefix * lastProduct
            else:
                prefix = nums[i - 1] * lastProduct
                lastProduct = prefix * lastProduct
            pre.append(prefix)
        
        print(f'pre[]: {pre}')

        lastProduct = 1
        i = len(nums) - 1
        while i >= 0:
            if i == len(nums) - 1:
                postfix = 1
                lastProduct = postfix * lastProduct
            else:
                postfix = nums[i - 1] * lastProduct
            post.append(postfix)
        
        print(f'post[]: {post}')


        return answer