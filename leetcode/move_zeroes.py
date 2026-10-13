#https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n=len(nums)
        has_zero=0
        for j in range(n):
            if nums[j]==0:
                k=j
                has_zero=1
                break
        if has_zero!=0:
            for j in range(k,n):
                if nums[j]!=0:
                    tmp=nums[j]
                    nums[j]=nums[k]
                    nums[k]=tmp
                    k+=1