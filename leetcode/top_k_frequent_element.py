#https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for j in range(len(nums)):
            if nums[j] not in d:
                d[nums[j]] = 0
            d[nums[j]] += 1

        f={}
        for key in d:
            if d[key] not in f:
                f[d[key]] = []
            f[d[key]].append(key)
        
        sf = [0] * (len(nums)+1)
        for j in range(len(nums)+1):
            if j in f:
                sf[j] = f[j]

        out = []
        r = 0
        j = 0
        l = len(nums)-1
        while r < k:
            if sf[l-j] != 0:
                out += sf[l-j]
                r += len(sf[l-j])
            j += 1
        
        return out[:k]