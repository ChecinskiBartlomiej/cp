#https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ds = {}
        dt = {}

        for j in range(len(s)):
            if s[j] not in ds:
                ds[s[j]] = 0
            ds[s[j]] += 1
            if t[j] not in dt:
                dt[t[j]] = 0
            dt[t[j]] += 1

        if ds == dt:
            return True
        else: return False