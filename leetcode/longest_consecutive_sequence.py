#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        S = set(nums)
        M = 0

        for x in S:
            if (x-1) not in S:
                c = 0
                while (x+c) in S:
                    c += 1
                M = max(M, c)
        return M