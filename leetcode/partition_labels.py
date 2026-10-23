#https://leetcode.com/problems/partition-labels/description/

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        n=len(s)
        out=[]
        last={}
        for j in range(n):
            last[s[j]]=j
        j=0
        while j<n:
            k=0
            M=last[s[j]]
            while j+k<=M:
                M=max(M,last[s[j+k]])
                k+=1
            out.append(k)
            j+=k
        return out
