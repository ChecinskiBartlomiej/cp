#https://leetcode.com/problems/beautiful-arrangement/description/

class Solution:
    def countArrangement(self, n: int) -> int:
        result=[]
        current=[]
        used=[False]*n

        def backtrack():
            if len(current)==n:
                result.append(current.copy())
                return
            for j in range(1,n+1):
                if used[j-1]==True or ((len(current)+1)%j!=0 and j%(len(current)+1)!=0):
                    continue
                used[j-1]=True
                current.append(j)
                backtrack()
                current.pop()
                used[j-1]=False

        backtrack()
        return len(result)