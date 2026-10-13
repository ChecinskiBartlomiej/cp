#https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        else: return False