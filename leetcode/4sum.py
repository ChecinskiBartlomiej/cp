#https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n=len(nums)
        out=[]
        nums.sort()
        for a in range(n-3):
            if a>0 and nums[a]==nums[a-1]:
                continue
            for b in range(a+1,n-2):
                if b>1 and b-1!=a and nums[b]==nums[b-1]:
                    continue
                c=b+1
                d=n-1
                while c<d:
                    s=nums[a]+nums[b]+nums[c]+nums[d]
                    if s==target:
                        out.append([nums[a],nums[b],nums[c],nums[d]])
                        c+=1
                        d-=1
                        while c<d and nums[c]==nums[c-1]:
                            c+=1
                        while c<d and nums[d]==nums[d+1]:
                            d-=1
                    elif s<target:
                        c+=1
                    else:
                        d-=1
        return out
