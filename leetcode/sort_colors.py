#https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def s(a,b,nums):
            n=len(nums)
            k=1
            for j in range(n):
                if nums[j]==b:
                    while j+k<n and nums[j+k]!=a:
                        k+=1
                    if j+k>=n:
                        break
                    nums[j],nums[j+k]=nums[j+k],nums[j]
        s(0,1,nums)
        s(0,2,nums)
        s(1,2,nums)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=1
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==c:
                mid+=1
            elif nums[mid]>c:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            elif nums[mid]<c:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1