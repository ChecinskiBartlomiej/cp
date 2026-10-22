#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H=haystack
        N=needle
        for j in range(len(H)-len(N)+1):
            k=1
            if H[j]==N[0]:
                while k<len(N) and H[j+k]==N[k]:
                    k+=1
                if k==len(N):
                    return j
        return -1
        
        