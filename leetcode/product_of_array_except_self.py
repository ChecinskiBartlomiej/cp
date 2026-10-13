#https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for j in range(n):
            answer[j] *= prefix
            prefix *= nums[j]

        suffix = 1
        for j in range(n-1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]
        return answer
