#https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result=[]
        current=[]
        def backtrack(j):
            if len(current)==k:
                result.append(current.copy())
                return
            for m in range(j+1,n+1):
                current.append(m)
                backtrack(m)
                current.pop()
        backtrack(0)
        return result