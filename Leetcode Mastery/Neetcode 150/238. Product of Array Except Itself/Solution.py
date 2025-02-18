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

        product = 0
        for i in range(len(nums)):
            if i == 0:
                prefix = 1 * nums[i]
                product = prefix
            else:
                prefix = product * nums[i - 1]
                product = prefix
            pre.append(prefix)

        product = 0
        i = len(nums) - 1
        while i >= 0:
            if i == len(nums) - 1:
                postfix = 1
                product = postfix
            else:
                postfix = product * nums[i + 1]
                product = postfix
            i -= 1
            post.append(postfix)
        post.reverse()

        for i in range(len(nums)):
            product = pre[i] * post[i]
            answer.append(product)

        print(f'pre[]: {pre}')
        print(f'post[]: {post}')

        return answer