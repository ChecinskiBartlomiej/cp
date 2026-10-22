#https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        k = 1

        for j in range(n):
            if nums[j] == val:
                while j + k < n and nums[j + k] == val:
                    k += 1

                if j + k == n:
                    return j

                nums[j], nums[j + k] = nums[j + k], nums[j]

        return n