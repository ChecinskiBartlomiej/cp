#https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=min(len(word1),len(word2))
        M=max(len(word1),len(word2))
        merged=""
        for j in range(m):
            merged+=word1[j]
            merged+=word2[j]
        if len(word1)>len(word2):
            for j in range(m,M):
                merged+=word1[j]
        else:
            for j in range(m,M):
                merged+=word2[j]
        return merged