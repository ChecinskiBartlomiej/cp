#https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        prefix = 0
        d[0] = 1
        l = 0

        for j in range(len(nums)):
            prefix += nums[j]
            if prefix - k in d:
                l += d[prefix-k]
            if prefix not in d:
                d[prefix] = 0
            d[prefix] += 1

        return l