#https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        current=[]

        def backtrack(j,total):
            if total==n and len(current)==k:
                result.append(current.copy())
                return
            for m in range(j,10):
                if total+m>n:
                    break
                current.append(m)
                backtrack(m+1,total+m)
                current.pop()

        backtrack(1,0)
        return result