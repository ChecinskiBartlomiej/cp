#https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[]
        current=[]
        def backtracking(i):
            if i==len(nums):
                result.append(current.copy())
                return

            backtracking(i+1)

            current.append(nums[i])
            backtracking(i+1)

            current.pop()
        
        backtracking(0)
        return result