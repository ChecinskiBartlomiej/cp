#https://leetcode.com/problems/3sum/description/

nums = [-1,0,1,2,-1,-4]

n = len(nums)

d = {}

for j in range(n):
    for k in range(j+1, n):
        key = - nums[j] - nums[k]
        if key not in d:
            d[key] = []
        d[key].append([(nums[j], j), (nums[k], k)])

print(d)

lists = []

for j in range(n):
    if nums[j] in d:
        for k in range(len(d[nums[j]])):
            pair = d[nums[j]][k]
            if j != pair[0][1] and j != pair[1][1]:
                lists.append([pair[0][0], pair[1][0], nums[j]])

print(lists)

triplets = []

for x in lists:
    t = tuple(sorted(x))
    triplets.append(t)

print(triplets)

sets = set()

for t in triplets:
    sets.add(t)

print(sets)

print([list(s) for s in sets])





