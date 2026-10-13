#https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1