#https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        k=0
        for j in range(len(t)):
            if t[j]==s[k]:
                k+=1
            if k==len(s):
                return True
        return False