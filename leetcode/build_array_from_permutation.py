#https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            ans.append(nums[x])
        return ans