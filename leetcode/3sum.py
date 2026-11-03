#https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        target=0
        out = []
        for left in range(n-2):
            if left>0 and nums[left]==nums[left-1]:
                continue
            mid=left+1
            right=n-1
            while mid<right:
                s=nums[left]+nums[mid]+nums[right]
                if s==target:
                    out.append([nums[left],nums[mid],nums[right]])
                    mid+=1
                    right-=1
                    while mid<right and nums[mid]==nums[mid-1]:
                        mid+=1
                    while mid<right and nums[right]==nums[right+1]:
                        right-=1
                elif s<target:
                    mid+=1
                else:
                    right-=1
        return out


