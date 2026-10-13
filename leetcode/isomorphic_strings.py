#https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d= {}
        taken = set()
        for j in range(len(s)):
            if s[j] not in d:
                if t[j] not in taken:
                    d[s[j]] = t[j]
                    taken.add(t[j])
                else:
                    return False
            else:
                if d[s[j]] != t[j]:
                    return False
        return True