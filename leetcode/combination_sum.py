#https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result=[]
        current=[]

        def backtrack(j, total):
            if total==target:
                result.append(current.copy())
                return
            for m in range(j, len(candidates)):
                if total+candidates[m]>target:
                    break
                current.append(candidates[m])
                backtrack(m,total+candidates[m])
                current.pop()

        backtrack(0,0)
        return result