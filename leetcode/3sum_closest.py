#https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        M=nums[0]+nums[1]+nums[2]
        for a in range(n-2):
            b=a+1
            c=n-1
            while b<c:
                s=nums[a]+nums[b]+nums[c]
                if s==target:
                    return s
                elif s<target:
                    if abs(s-target)<abs(M-target):
                        M=s
                    b+=1
                else:
                    if abs(s-target)<abs(M-target):
                        M=s
                    c-=1
        return M