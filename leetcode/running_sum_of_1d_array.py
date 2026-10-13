#https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        rS = 0
        rSl = []
        for j in range(len(nums)):
            rS += nums[j]
            rSl.append(rS)
        return rSl