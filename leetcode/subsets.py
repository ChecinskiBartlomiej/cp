nums = [1,2,3,4,5]

subsets = []
subsets.append([])
for j in range(len(nums)):
    new_subsets = []
    for s in subsets:
        t = list(s)
        t.append(nums[j])
        new_subsets.append(t)
    for s in new_subsets:
        subsets.append(s)

print(subsets)
print(len(subsets))