#https://leetcode.com/problems/reverse-string-ii/description/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(start,end,s):
            a=start
            b=end
            while a<b:
                s[a],s[b]=s[b],s[a]
                a+=1
                b-=1
            return s
        s=list(s)
        n=len(s)
        p=n//(2*k)
        r=n%(2*k)
        for i in range(p):
            start=2*k*i
            end=2*k*i+k-1
            reverse(start,end,s)
        if r<k:
            start=2*k*p
            end=2*k*p+r-1
            reverse(start,end,s)
        elif r>=k:
            start=2*k*p
            end=2*k*p+k-1
            reverse(start,end,s)
        s="".join(s)
        return s