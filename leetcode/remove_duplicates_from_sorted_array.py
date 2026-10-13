#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1

        for j in range(1,len(nums)):
            if nums[j] != nums[k-1]:
                nums[k] = nums[j]
                k += 1
        return k