#https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true

s = 'abaacdabd'

unique = set(s)
unique_list = list(unique)
pairs = []

for j in range(len(unique_list)):
    for k in range(j+1, len(unique_list)):
        pairs.append((unique_list[j], unique_list[k]))


M = 0
for pair in pairs:
    t = list(s)
    new = []
    l = 1
    for j in range(len(s)):
        if t[j] in pair:
            new.append(t[j])
    for j in range(len(new)-1):
        if new[j] == new[j+1]:
            l = 0
            break
        else:
            l += 1
    M = max(l, M)

print(M)

    



