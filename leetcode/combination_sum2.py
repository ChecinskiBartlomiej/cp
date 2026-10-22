#https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result=[]
        current=[]

        def backtrack(j, total):
            if total==target:
                result.append(current.copy())
                return
            for m in range(j, len(candidates)):
                if m>j and candidates[m-1]==candidates[m]:
                    continue
                if total+candidates[m]>target:
                    break
                current.append(candidates[m])
                backtrack(m+1,total+candidates[m])
                current.pop()

        backtrack(0,0)
        return result