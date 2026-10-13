#https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = 0
        right = n-1
        out = [0] * n
        k = n-1

        while left < right:
            if nums[left]*nums[left] >= nums[right]*nums[right]:
                out[k]=nums[left]*nums[left]
                left+=1
            else:
                out[k]=nums[right]*nums[right]
                right-=1
            k-=1
        out[k]=nums[right]*nums[right]

        return out