#https://leetcode.com/problems/permutations-ii/description/?envType=problem-list-v2&envId=backtracking

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result=[]
        current=[]
        used=[False]*len(nums)
        nums.sort()
        def backtrack():
            if len(current)==len(nums):
                result.append(current.copy())
                return
            for j in range(len(nums)):
                if used[j]:
                    continue
                if j>0 and nums[j-1]==nums[j] and used[j-1]==False:
                    continue
                used[j]=True
                current.append(nums[j])
                backtrack()
                current.pop()
                used[j]=False
        backtrack()
        return result