#https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        out=0
        for j in range(len(arr1)):
            for k in range(len(arr2)):
                if abs(arr1[j]-arr2[k])<=d:
                    out-=1
                    break
            out+=1
        return out