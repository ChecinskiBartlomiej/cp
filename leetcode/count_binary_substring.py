#https://leetcode.com/problems/count-binary-substrings/description/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev=0
        curr=1
        out=0

        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                curr+=1
            else:
                out+=min(prev,curr)
                prev=curr
                curr=1

        out+=min(prev,curr)
        return out