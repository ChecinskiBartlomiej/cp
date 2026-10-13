#https://leetcode.com/problems/intersection-of-two-arrays/description/

nums1 = [1,2,2,1]
nums2 = [2,2]

n1 = set(nums1)
n2 = set(nums2)
out = []

for x in n1:
    if x in n2:
        out.append(x)

print(out)
