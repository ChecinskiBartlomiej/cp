#https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=backtracking

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations=[[nums[0]]]
        for j in range(1,len(nums)):
            new=[]
            for p in permutations:
                for k in range(len(p)+1):
                    q=p.copy()
                    q.insert(k,nums[j])
                    new.append(q)
            permutations=new
        return permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=[]
        current=[]
        used=[False]*len(nums)
        def backtrack():
            if len(current)==len(nums):
                result.append(current.copy())
                return
            for j in range(len(nums)):
                if used[j]==True:
                    continue
                used[j]=True
                current.append(nums[j])
                backtrack()
                current.pop()
                used[j]=False
        backtrack()
        return result
